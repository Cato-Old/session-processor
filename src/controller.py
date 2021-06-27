from typing import Generator

from src.domain import Statement
from src.grouper import StatementGrouper
from src.sorter import StatementSorter


class SessionProcessorController:
    def __init__(
            self,
            grouper: StatementGrouper,
            sorter: StatementSorter,
    ) -> None:
        self._grouper = grouper

    def process(
            self, input_statements: Generator[Statement, None, None],
    ) -> None:
        self._grouper.group(input_statements)
        raise NotImplementedError
