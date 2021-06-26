import datetime
from abc import ABC
from abc import abstractmethod
from csv import DictReader
from typing import Generator
from typing import Tuple

from src.domain import Statement

SplitDate = Tuple[int, int, int, int, int, int]


class Loader(ABC):
    @abstractmethod
    def load(self, path: str) -> Generator[Statement, None, None]:
        raise NotImplementedError


class PSVLoader(Loader):
    def load(self, path: str) -> Generator[Statement, None, None]:
        with open(path, mode='r') as f:
            reader = DictReader(f, delimiter='|')
            for row in reader:
                yield Statement(
                    int(row['HomeNo']),
                    int(row['Channel']),
                    datetime.datetime(*self._split_raw_date(row['Starttime'])),
                    row['Activity'],
                )

    @staticmethod
    def _split_raw_date(raw_date: str) -> SplitDate:
        return (
            int(raw_date[0:4]),
            int(raw_date[4:6]),
            int(raw_date[6:8]),
            int(raw_date[8:10]),
            int(raw_date[10:12]),
            int(raw_date[12:14]),
        )
