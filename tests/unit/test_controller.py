from pytest import fixture

from src.controller import SessionProcessorController


class TestSessionProcessorController:
    @fixture
    def controller(self) -> SessionProcessorController:
        return SessionProcessorController()

    def test_can_instantiate(
            self, controller: SessionProcessorController,
    ) -> None:
        pass

