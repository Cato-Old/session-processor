from mockito import mock
from pytest import fixture
from pytest import raises

from src.app import Application
from src.view import SessionProcessorView


class TestApplication:
    @fixture
    def view(self) -> SessionProcessorView:
        return mock()

    @fixture
    def app(self, view: SessionProcessorView) -> Application:
        return Application(view=view)

    def test_raises_on_run(self, app: Application) -> None:
        with raises(NotImplementedError):
            app.run()
