from datetime import datetime
from typing import List
from uuid import UUID

from domain.entities.file import FileHashType


class CheckedReportInterface:
    reportidentifier: UUID
    date: datetime
    hash_algo: FileHashType
    workers: int
    modified_files: List[str]
    missing_files: List[str]
    added_files: List[str]
    errors: List[str]
