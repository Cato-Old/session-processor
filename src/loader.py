from abc import ABC
from abc import abstractmethod


class Loader(ABC):
    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError


class PSVLoader(Loader):
    def load(self) -> None:
        raise NotImplementedError
