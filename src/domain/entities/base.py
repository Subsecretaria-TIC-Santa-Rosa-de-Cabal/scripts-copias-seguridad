from datetime import datetime
from uuid import UUID


class Base:
    def __init__(
            self,
            identifier: UUID,
            enabled: bool,
            registration_date: datetime,
            last_update: datetime
        ):
        self.__identifier = identifier
        self.__enabled = enabled
        self.__registration_date = registration_date
        self.__last_update = last_update

    @property
    def identifier(self) -> UUID:
        return self.__identifier

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @property
    def registration_date(self) -> datetime:
        return self.__registration_date

    @property
    def last_update(self) -> datetime:
        return self.__last_update
