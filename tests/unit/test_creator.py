from typing import Dict, List

from factory.fuzzy import FuzzyInteger
from pytest import fixture
from pytest import raises

from src.creator import SessionCreator
from src.domain import Statement
from tests.unit.test_loader import StatementFactory


class TestSessionCreator:
    @fixture
    def creator(self) -> SessionCreator:
        return SessionCreator()

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

    def test_raise_on_creation(
            self,
            creator: SessionCreator,
            sorted_statements: Dict[int, List[Statement]],
    ) -> None:
        with raises(NotImplementedError):
            creator.create(sorted_statements)
