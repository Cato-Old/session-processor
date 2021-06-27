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
from src.creator import SessionCreator
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
    def sorted_statements(self) -> Dict[int, List[Statement]]:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        statements = {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }
        for statement in statements:
            statements[statement].sort(key=lambda s: s.start_time)
        return statements

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
    def sorter(
            self,
            grouped_statements: Dict[int, List[Statement]],
            sorted_statements: Dict[int, List[Statement]],
    ) -> StatementSorter:
        sorter = mock(StatementSorter)
        when(sorter).sort(grouped_statements).thenReturn(sorted_statements)
        return sorter

    @fixture
    def creator(self) -> SessionCreator:
        return mock(SessionCreator)

    @fixture
    def controller(
            self,
            grouper: StatementGrouper,
            sorter: StatementSorter,
            creator: SessionCreator,
    ) -> SessionProcessorController:
        return SessionProcessorController(
            grouper=grouper, sorter=sorter, creator=creator,
        )

    def test_raises_on_process(
            self,
            controller: SessionProcessorController,
            grouper: StatementGrouper,
            sorter: StatementSorter,
            input_statements: Generator[Statement, None, None],
    ) -> None:
        with raises(NotImplementedError):
            controller.process(input_statements)
        verify(grouper).group(...)
        verify(sorter).sort(...)
