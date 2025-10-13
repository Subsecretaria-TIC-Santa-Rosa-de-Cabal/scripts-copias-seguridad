from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
import json
import os
from uuid import uuid4

from tqdm import tqdm

from domain.entities.file import FileHashType
from domain.entities.report import Report
from domain.repositories.file_repository import FileRepository
from domain.repositories.interfaces.report_interface import CheckedReportInterface
from domain.repositories.report_repository import ReportRepository
from infrastructure.persistence.json.config import JSON_DB_FOLDER


class JsonReportRepository(ReportRepository):
    IGNORE_DIRS = {
        "$recycle.bin",
        "system volume information",
        ".trash",
        ".ds_store",
        ".spotlight-v100"
    }

    def __should_ignore(self, path):
        """Check if a folder or file should be ignored."""
        parts = [p.lower() for p in os.path.normpath(path).split(os.sep)]
        return any(part in self.IGNORE_DIRS for part in parts)

    def generate(
        self,
        root_path: str,
        hash_type: FileHashType,
        workers: int,
        file_repository: FileRepository
    ) -> Report:
        file_paths = []
        for folder, _, files in os.walk(root_path):
            if self.__should_ignore(folder):
                continue
            for name in files:
                path = os.path.join(folder, name)
                if not self.__should_ignore(path):
                    file_paths.append(path)
        
        data = {}

        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(file_repository.get_from_path, path, hash_type) for path in file_paths]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Generating report", unit="file"):
                result = future.result()
                data[result] = result

        response = Report(
            identifier = uuid4(),
            enabled = True,
            registration_date = datetime.now(),
            last_update = datetime.now(),
            root_path = root_path,
            files = data
        )

        reports_folder = JSON_DB_FOLDER + 'reports/'
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder, exist_ok=True)

        with open(
            reports_folder + str(response.registration_date).replace(':', '-').replace('.', '-') + '.json',
            "w",
            encoding="utf-8"
        ) as f:
            file_data = []
            for d in data:
                file_data.append({
                    'identifier': str(d.identifier),
                    'enabled': d.enabled,
                    'registration_date': str(d.registration_date),
                    'last_update': str(d.last_update),
                    'name': d.name,
                    'extension': d.extension,
                    'size': d.size,
                    'path': d.path,
                    'hash_digest': d.hash_digest,
                    'hash_type': d.hash_type.value if d.hash_type else None
                })
            json_data = {
                'identifier': str(response.identifier),
                'enabled': response.enabled,
                'registration_date': str(response.registration_date),
                'last_update': str(response.last_update),
                'root_path': root_path,
                'files': file_data
            }
            json.dump(json_data, f, indent=2, ensure_ascii=False, default=str)

        return response

    def verify(self, root_path: str, hash_type: FileHashType) -> CheckedReportInterface:
        pass
