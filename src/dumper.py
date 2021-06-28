from abc import ABC
from abc import abstractmethod

from src.domain import SessionGenerator


class Dumper(ABC):
    @abstractmethod
    def dump(self, sessions: SessionGenerator) -> None:
        raise NotImplementedError


class PSVDumper(Dumper):
    def dump(self, sessions: SessionGenerator) -> None:
        raise NotImplementedError
