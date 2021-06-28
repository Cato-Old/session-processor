from collections import defaultdict
from typing import List

from pytest import fixture

from src.domain import Statement
from src.domain import StatementGenerator
from src.domain import StatementsByHomeNo
from src.controller.grouper import StatementGrouper

from tests.unit.test_loader import StatementFactory


class TestStatementGrouper:
    @fixture
    def statement_values(self) -> List[Statement]:
        return StatementFactory.build_batch(10)

    @fixture
    def statements(
            self, statement_values: List[Statement],
    ) -> StatementGenerator:
        return (s for s in statement_values)

    @fixture
    def expected(
            self, statement_values: List[Statement],
    ) -> StatementsByHomeNo:
        grouped = defaultdict(lambda: [])
        for statement in statement_values:
            grouped[statement.home_no].append(statement)
        return grouped

    @fixture
    def grouper(self) -> StatementGrouper:
        return StatementGrouper()

    def test_groups_statements_by_home_no(
            self,
            grouper: StatementGrouper,
            statements: StatementGenerator,
            expected: StatementsByHomeNo,
    ) -> None:
        actual = grouper.group(statements)
        assert actual == expected
