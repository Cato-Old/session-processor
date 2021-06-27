from pytest import fixture

from src.sorter import StatementSorter


class TestStatementSorter:
    @fixture
    def sorter(self) -> StatementSorter:
        return StatementSorter()

    def test_can_instantiate(self, sorter: StatementSorter) -> None:
        pass
