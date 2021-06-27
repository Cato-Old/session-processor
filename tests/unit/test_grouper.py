from collections.abc import Generator

from pytest import fixture
from pytest import raises

from src.domain import Statement
from src.grouper import StatementGrouper

from tests.unit.test_loader import StatementFactory


class TestStatementGrouper:
    @fixture
    def statements(self) -> Generator[Statement, None, None]:
        return (StatementFactory() for _ in range(10))

    @fixture
    def grouper(self) -> StatementGrouper:
        return StatementGrouper()

    def test_raises_on_group(
            self,
            grouper: StatementGrouper,
            statements: Generator[Statement, None, None],
    ) -> None:
        with raises(NotImplementedError):
            grouper.group(statements)
