from factory.fuzzy import FuzzyText
from mockito import mock, when, verify
from pytest import fixture

from src.controller.controller import SessionProcessorController
from src.domain import SessionGenerator
from src.domain import StatementGenerator
from src.view.dumper import Dumper
from src.view.loader import Loader, PSVLoader
from src.view.view import SessionProcessorView

from tests.unit.controller.test_creator import SessionFactory
from tests.unit.view.test_loader import StatementFactory


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
    def output_path(self) -> str:
        return 'output_example.psv'

    @fixture
    def dumper(self, sessions: SessionGenerator, output_path: str) -> Dumper:
        dumper = mock(Dumper)
        when(dumper).dump(sessions, output_path)
        return dumper

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

    def test_processes_statements(
            self,
            view: SessionProcessorView,
            path: str,
            output_path: str,
            loader: Loader,
            controller: SessionProcessorController,
            dumper: Dumper,
    ) -> None:
        view.process(path, output_path)
        verify(loader).load(...)
        verify(controller).process(...)
        verify(dumper).dump(...)
