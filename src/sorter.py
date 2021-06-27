from typing import Dict
from typing import List

from src.domain import Statement


class StatementSorter:
    @staticmethod
    def sort(grouped_statement: Dict[int, List[Statement]]) -> None:
        raise NotImplementedError
