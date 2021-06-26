from tempfile import NamedTemporaryFile

from pytest import fixture
from pytest import raises

from src.loader import PSVLoader


class TestPSVLoader:
    @fixture
    def psv_file(self) -> NamedTemporaryFile:
        with NamedTemporaryFile() as ntf:
            yield ntf

    @fixture
    def loader(self, psv_file: NamedTemporaryFile) -> PSVLoader:
        return PSVLoader()

    @fixture
    def path(self, psv_file: NamedTemporaryFile) -> str:
        return psv_file.name

    def test_raises_on_load(self, loader: PSVLoader, path: str) -> None:
        with raises(NotImplementedError):
            loader.load(path)
