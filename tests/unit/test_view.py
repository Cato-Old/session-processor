from factory.fuzzy import FuzzyText
from mockito import mock
from pytest import fixture
from pytest import raises

from src.loader import Loader
from src.view import SessionProcessorView
from tests.unit.test_loader import StatementFactory


class TestSessionProcessorView:
    @fixture
    def path(self) -> str:
        return FuzzyText().fuzz()

    @fixture
    def loader(self) -> Loader:
        return mock()

    @fixture
    def view(self, loader: Loader) -> SessionProcessorView:
        return SessionProcessorView(loader=loader)

    def test_raises_on_process(
            self, view: SessionProcessorView, path: str,
    ) -> None:
        with raises(NotImplementedError):
            view.process(path)
