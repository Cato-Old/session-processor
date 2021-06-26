from pytest import fixture
from pytest import raises

from src.view import SessionProcessorView


class TestSessionProcessorView:
    @fixture
    def view(self) -> SessionProcessorView:
        return SessionProcessorView()

    def test_raises_on_process(self, view: SessionProcessorView) -> None:
        with raises(NotImplementedError):
            view.process()
