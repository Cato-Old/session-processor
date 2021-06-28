from src.controller.controller import SessionProcessorController
from src.loader import Loader


class SessionProcessorView:
    def __init__(
            self, loader: Loader, controller: SessionProcessorController,
    ) -> None:
        self._loader = loader
        self._controller = controller

    def process(self, path: str) -> None:
        statements = self._loader.load(path)
        self._controller.process(statements)
        raise NotImplementedError
