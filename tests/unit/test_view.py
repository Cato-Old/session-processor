from factory.fuzzy import FuzzyText
from mockito import mock, when, verify
from pytest import fixture
from pytest import raises

from src.controller.controller import SessionProcessorController
from src.loader import Loader, PSVLoader
from src.view import SessionProcessorView

from tests.unit.test_loader import StatementFactory


class TestSessionProcessorView:
    @fixture
    def path(self) -> str:
        return FuzzyText().fuzz()

    @fixture
    def loader(self, path: str) -> Loader:
        statements = StatementFactory.build_batch(10)
        loader = mock(PSVLoader)
        when(loader).load(path).thenReturn(s for s in statements)
        return loader

    @fixture
    def controller(self) -> SessionProcessorController:
        return mock(SessionProcessorController)

    @fixture
    def view(
            self, loader: Loader, controller: SessionProcessorController,
    ) -> SessionProcessorView:
        return SessionProcessorView(loader=loader, controller=controller)

    def test_raises_on_process(
            self, view: SessionProcessorView, path: str, loader: Loader,
    ) -> None:
        with raises(NotImplementedError):
            view.process(path)
        verify(loader).load(...)
