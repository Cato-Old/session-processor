from src.controller.creator import SessionCreator
from src.domain import SessionGenerator
from src.domain import StatementGenerator
from src.controller.grouper import StatementGrouper
from src.controller.sorter import StatementSorter


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
            self, input_statements: StatementGenerator,
    ) -> SessionGenerator:
        grouped = self._grouper.group(input_statements)
        sorted_statements = self._sorter.sort(grouped)
        return self._creator.create(sorted_statements)
