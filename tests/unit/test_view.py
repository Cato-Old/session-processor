from factory.fuzzy import FuzzyText
from mockito import mock, when, verify
from pytest import fixture
from pytest import raises

from src.controller.controller import SessionProcessorController
from src.domain import SessionGenerator
from src.domain import StatementGenerator
from src.dumper import Dumper
from src.loader import Loader, PSVLoader
from src.view import SessionProcessorView
from tests.unit.controller.test_creator import SessionFactory

from tests.unit.test_loader import StatementFactory


class TestSessionProcessorView:
    @fixture
    def path(self) -> str:
        return FuzzyText().fuzz()

    @fixture
    def statements(self) -> StatementGenerator:
        return (s for s in StatementFactory.build_batch(10))

    @fixture
    def loader(self, path: str, statements: StatementGenerator) -> Loader:
        loader = mock(PSVLoader)
        when(loader).load(path).thenReturn(statements)
        return loader

    @fixture
    def sessions(self) -> SessionGenerator:
        return (s for s in SessionFactory.build_batch(10))

    @fixture
    def controller(
            self,
            statements: StatementGenerator,
            sessions: SessionGenerator,
    ) -> SessionProcessorController:
        controller = mock(SessionProcessorController)
        when(controller).process(statements).thenReturn(sessions)
        return controller

    @fixture
    def dumper(self) -> Dumper:
        return mock(Dumper)

    @fixture
    def view(
            self,
            loader: Loader,
            controller: SessionProcessorController,
            dumper: Dumper
    ) -> SessionProcessorView:
        return SessionProcessorView(
            loader=loader, controller=controller, dumper=dumper,
        )

    def test_raises_on_process(
            self,
            view: SessionProcessorView,
            path: str,
            loader: Loader,
            controller: SessionProcessorController,
    ) -> None:
        with raises(NotImplementedError):
            view.process(path)
        verify(loader).load(...)
        verify(controller).process(...)
