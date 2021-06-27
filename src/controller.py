from typing import Generator

from src.creator import SessionCreator
from src.domain import Statement
from src.grouper import StatementGrouper
from src.sorter import StatementSorter


class SessionProcessorController:
    def __init__(
            self,
            grouper: StatementGrouper,
            sorter: StatementSorter,
            creator: SessionCreator,
    ) -> None:
        self._grouper = grouper
        self._sorter = sorter

    def process(
            self, input_statements: Generator[Statement, None, None],
    ) -> None:
        grouped = self._grouper.group(input_statements)
        self._sorter.sort(grouped)
        raise NotImplementedError
