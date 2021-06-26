from src.loader import Loader


class SessionProcessorView:
    def __init__(self, loader: Loader) -> None:
        pass

    def process(self) -> None:
        raise NotImplementedError
