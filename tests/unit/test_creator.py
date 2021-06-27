from pytest import fixture

from src.creator import SessionCreator


class TestSessionCreator:
    @fixture
    def creator(self) -> SessionCreator:
        return SessionCreator()

    def test_can_instantiate(self, creator: SessionCreator) -> None:
        pass
