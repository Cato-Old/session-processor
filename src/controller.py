from typing import Generator

from src.creator import SessionCreator
from src.domain import Statement, Session
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
        self._creator = creator

    def process(
            self, input_statements: Generator[Statement, None, None],
    ) -> Generator[Session, None, None]:
        grouped = self._grouper.group(input_statements)
        sorted_statements = self._sorter.sort(grouped)
        return self._creator.create(sorted_statements)
