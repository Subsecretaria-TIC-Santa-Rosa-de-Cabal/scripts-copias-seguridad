from datetime import datetime
from enum import Enum, unique
from typing import List
from uuid import UUID

from domain.entities.base import Base
from domain.entities.file import File


class Report(Base):
    def __init__(
            self,
            identifier: UUID,
            enabled: bool,
            registration_date: datetime,
            last_update: datetime,
            root_path: str,
            files: List[File],
        ):
        super().__init__(
            identifier,
            enabled,
            registration_date,
            last_update,
        )
        self.__root_path = root_path
        self.__files = files

    @property
    def root_path(self) -> str:
        return self.__root_path
    
    @property
    def files(self) -> List[File]:
        return self.__files
