from typing import Dict
from typing import List

from src.domain import Statement


class StatementSorter:
    @staticmethod
    def sort(
            grouped_statement: Dict[int, List[Statement]],
    ) -> Dict[int, List[Statement]]:
        for key in grouped_statement:
            grouped_statement[key].sort(key=lambda s: s.start_time)
        return grouped_statement
