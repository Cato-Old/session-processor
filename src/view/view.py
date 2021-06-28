from src.controller.controller import SessionProcessorController
from src.view.dumper import Dumper
from src.view.loader import Loader


class SessionProcessorView:
    def __init__(
            self,
            loader: Loader,
            controller: SessionProcessorController,
            dumper: Dumper,
    ) -> None:
        self._loader = loader
        self._controller = controller
        self._dumper = dumper

    def process(self, path: str, output_path: str) -> None:
        statements = self._loader.load(path)
        sessions = self._controller.process(statements)
        self._dumper.dump(sessions, output_path)
