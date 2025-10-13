from abc import ABC, abstractmethod

from domain.entities.file import FileHashType
from domain.entities.report import Report
from domain.repositories.file_repository import FileRepository
from domain.repositories.interfaces.report_interface import CheckedReportInterface


class ReportRepository(ABC):
    @abstractmethod
    def generate(
        self,
        root_path: str,
        hash_type: FileHashType,
        workers: int,
        file_repository: FileRepository
    ) -> Report:
        pass

    @abstractmethod
    def verify(self, root_path: str, hash_type: FileHashType) -> CheckedReportInterface:
        pass
