from collections import defaultdict
from collections.abc import Generator
from typing import Dict
from typing import List

from pytest import fixture

from src.domain import Statement
from src.grouper import StatementGrouper

from tests.unit.test_loader import StatementFactory


class TestStatementGrouper:
    @fixture
    def statement_values(self) -> List[Statement]:
        return StatementFactory.build_batch(10)

    @fixture
    def statements(
            self, statement_values: List[Statement],
    ) -> Generator[Statement, None, None]:
        return (s for s in statement_values)

    @fixture
    def expected(
            self, statement_values: List[Statement],
    ) -> Dict[str, List[Statement]]:
        grouped = defaultdict(lambda: [])
        for statement in statement_values:
            grouped[statement.home_no].append(statement)
        return grouped

    @fixture
    def grouper(self) -> StatementGrouper:
        return StatementGrouper()

    def test_raises_on_group(
            self,
            grouper: StatementGrouper,
            statements: Generator[Statement, None, None],
            expected: Dict[str, List[Statement]],
    ) -> None:
        actual = grouper.group(statements)
        assert actual == expected
