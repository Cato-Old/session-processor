from factory.fuzzy import FuzzyInteger
from pytest import fixture

from src.domain import StatementsByHomeNo
from src.controller.sorter import StatementSorter
from tests.unit.view.test_loader import StatementFactory


class TestStatementSorter:
    @fixture
    def sorter(self) -> StatementSorter:
        return StatementSorter()

    @fixture
    def grouped(self) -> StatementsByHomeNo:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        return {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }

    @fixture
    def expected(self, grouped: StatementsByHomeNo) -> StatementsByHomeNo:
        for key in grouped:
            grouped[key].sort(key=lambda s: s.start_time)
        return grouped

    def test_sorts_statements_by_start_time(
            self,
            sorter: StatementSorter,
            grouped: StatementsByHomeNo,
            expected: StatementsByHomeNo,
    ) -> None:
        actual = sorter.sort(grouped)
        assert actual == expected
