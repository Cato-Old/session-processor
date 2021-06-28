from src.controller.controller import SessionProcessorController
from src.loader import Loader


class SessionProcessorView:
    def __init__(
            self, loader: Loader, controller: SessionProcessorController,
    ) -> None:
        self._loader = loader

    def process(self, path: str) -> None:
        self._loader.load(path)
        raise NotImplementedError
