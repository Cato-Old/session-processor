from typing import Generator

from pytest import fixture
from pytest import raises

from src.controller import SessionProcessorController
from src.domain import Statement

from tests.unit.test_loader import StatementFactory


class TestSessionProcessorController:
    @fixture
    def input_statements(self) -> Generator[Statement, None, None]:
        statements = StatementFactory.build_batch(10)
        return (s for s in statements)

    @fixture
    def controller(self) -> SessionProcessorController:
        return SessionProcessorController()

    def test_raises_on_process(
            self,
            controller: SessionProcessorController,
            input_statements: Generator[Statement, None, None],
    ) -> None:
        with raises(NotImplementedError):
            controller.process(input_statements)
