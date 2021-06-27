from typing import Generator

from src.domain import Statement
from src.grouper import StatementGrouper


class SessionProcessorController:
    def __init__(self, grouper: StatementGrouper) -> None:
        self._grouper = grouper

    def process(
            self, input_statements: Generator[Statement, None, None],
    ) -> None:
        self._grouper.group(input_statements)
        raise NotImplementedError
