from typing import Dict
from typing import Generator
from typing import List

from src.domain import Statement


class StatementGrouper:
    @staticmethod
    def group(
            statements: Generator[Statement, None, None],
    ) -> Dict[int, List[Statement]]:
        grouped = {}
        for statement in statements:
            try:
                grouped[statement.home_no].append(statement)
            except KeyError:
                grouped[statement.home_no] = [statement]
        return grouped
