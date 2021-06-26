from pytest import fixture
from pytest import raises

from src.loader import PSVLoader


class TestPSVLoader:
    @fixture
    def loader(self) -> PSVLoader:
        return PSVLoader()

    def test_raises_on_load(self, loader: PSVLoader) -> None:
        with raises(NotImplementedError):
            loader.load()
