from typing import List

from factory.fuzzy import FuzzyInteger
from mockito import mock
from mockito import when
from pytest import fixture

from src.controller import SessionProcessorController
from src.creator import SessionCreator
from src.domain import Session
from src.domain import StatementGenerator
from src.domain import StatementsByHomeNo
from src.grouper import StatementGrouper
from src.sorter import StatementSorter

from tests.unit.test_creator import SessionFactory
from tests.unit.test_loader import StatementFactory


class TestSessionProcessorController:
    @fixture
    def input_statements(self) -> StatementGenerator:
        statements = StatementFactory.build_batch(10)
        return (s for s in statements)

    @fixture
    def grouped(self) -> StatementsByHomeNo:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        return {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }

    @fixture
    def sorted_by_time(self) -> StatementsByHomeNo:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        statements = {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }
        for statement in statements:
            statements[statement].sort(key=lambda s: s.start_time)
        return statements

    @fixture
    def sessions(self) -> List[Session]:
        return SessionFactory.build_batch(10)

    @fixture
    def grouper(
            self,
            input_statements: StatementGenerator,
            grouped: StatementsByHomeNo,
    ) -> StatementGrouper:
        grouper = mock(StatementGrouper)
        when(grouper).group(input_statements).thenReturn(grouped)
        return grouper

    @fixture
    def sorter(
            self,
            grouped: StatementsByHomeNo,
            sorted_by_time: StatementsByHomeNo,
    ) -> StatementSorter:
        sorter = mock(StatementSorter)
        when(sorter).sort(grouped).thenReturn(sorted_by_time)
        return sorter

    @fixture
    def creator(
            self,
            sorted_by_time: StatementsByHomeNo,
            sessions: List[Session],
    ) -> SessionCreator:
        creator = mock(SessionCreator)
        when(creator).create(sorted_by_time).thenReturn(s for s in sessions)
        return creator

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
            creator: SessionCreator,
            input_statements: StatementGenerator,
            sessions: List[Session],
    ) -> None:
        actual = controller.process(input_statements)
        assert list(actual) == sessions
