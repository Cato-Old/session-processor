from typing import Dict, List

from factory.fuzzy import FuzzyInteger
from pytest import fixture

from src.domain import Statement
from src.sorter import StatementSorter
from tests.unit.test_loader import StatementFactory


class TestStatementSorter:
    @fixture
    def sorter(self) -> StatementSorter:
        return StatementSorter()

    @fixture
    def grouped_statements(self) -> Dict[int, List[Statement]]:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        return {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }

    @fixture
    def expected(
            self, grouped_statements: Dict[int, List[Statement]],
    ) -> Dict[int, List[Statement]]:
        for key in grouped_statements:
            grouped_statements[key].sort(key=lambda s: s.start_time)
        return grouped_statements

    def test_raise_on_sort_method(
            self,
            sorter: StatementSorter,
            grouped_statements: Dict[int, List[Statement]],
            expected: Dict[int, List[Statement]],
    ) -> None:
        actual = sorter.sort(grouped_statements)
        assert actual == expected
