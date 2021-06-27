from typing import Dict
from typing import List

from src.domain import Statement


class SessionCreator:
    def create(self, sorted_statements: Dict[int, List[Statement]]) -> None:
        raise NotImplementedError
