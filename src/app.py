import sys

from src.view.view import SessionProcessorView


class Application:
    def __init__(self, view: SessionProcessorView) -> None:
        self._view = view

    def run(self) -> None:
        arguments = sys.argv[1:]
        self._view.process(*arguments)
