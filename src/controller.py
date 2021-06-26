from typing import Generator

from src.domain import Statement


class SessionProcessorController:
    def process(
            self, input_statements: Generator[Statement, None, None],
    ) -> None:
        raise NotImplementedError
