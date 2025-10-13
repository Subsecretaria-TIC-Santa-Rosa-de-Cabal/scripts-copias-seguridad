from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.file import File, FileHashType


class FileRepository(ABC):
    @abstractmethod
    def get_from_path(self, file_path: str, hash_type: Optional[FileHashType]) -> File:
        pass

    @abstractmethod
    def delete(self, file_path: str) -> File:
        pass
