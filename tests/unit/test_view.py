from mockito import mock
from pytest import fixture
from pytest import raises

from src.loader import Loader
from src.view import SessionProcessorView


class TestSessionProcessorView:
    @fixture
    def loader(self) -> Loader:
        return mock()

    @fixture
    def view(self, loader: Loader) -> SessionProcessorView:
        return SessionProcessorView(loader=loader)

    def test_raises_on_process(self, view: SessionProcessorView) -> None:
        with raises(NotImplementedError):
            view.process()
