from typing import Generator

from src.domain import Statement


class StatementGrouper:
    def group(self, statements: Generator[Statement, None, None]) -> None:
        raise NotImplementedError
