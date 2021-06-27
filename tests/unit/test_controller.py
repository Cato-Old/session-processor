from typing import Dict
from typing import Generator
from typing import List

from factory.fuzzy import FuzzyInteger
from mockito import mock
from mockito import verify
from mockito import when
from pytest import fixture
from pytest import raises

from src.controller import SessionProcessorController
from src.domain import Statement
from src.grouper import StatementGrouper
from src.sorter import StatementSorter

from tests.unit.test_loader import StatementFactory


class TestSessionProcessorController:
    @fixture
    def input_statements(self) -> Generator[Statement, None, None]:
        statements = StatementFactory.build_batch(10)
        return (s for s in statements)

    @fixture
    def grouped_statements(self) -> Dict[int, List[Statement]]:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        return {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }

    @fixture
    def grouper(
            self,
            input_statements: Generator[Statement, None, None],
            grouped_statements: Dict[int, List[Statement]],
    ) -> StatementGrouper:
        grouper = mock(StatementGrouper)
        when(grouper).group(input_statements).thenReturn(grouped_statements)
        return grouper

    @fixture
    def sorter(self) -> StatementSorter:
        return mock(StatementSorter)

    @fixture
    def controller(
            self, grouper: StatementGrouper, sorter: StatementSorter,
    ) -> SessionProcessorController:
        return SessionProcessorController(grouper=grouper, sorter=sorter)

    def test_raises_on_process(
            self,
            controller: SessionProcessorController,
            grouper: StatementGrouper,
            input_statements: Generator[Statement, None, None],
    ) -> None:
        with raises(NotImplementedError):
            controller.process(input_statements)
        verify(grouper).group(...)
