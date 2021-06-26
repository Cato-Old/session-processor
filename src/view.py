from src.loader import Loader


class SessionProcessorView:
    def __init__(self, loader: Loader) -> None:
        self._loader = loader

    def process(self, path: str) -> None:
        self._loader.load(path)
        raise NotImplementedError
