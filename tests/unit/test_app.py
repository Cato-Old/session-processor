from unittest.mock import patch

from mockito import mock, when
from pytest import fixture

from src.app import Application
from src.view.view import SessionProcessorView


class TestApplication:
    @fixture
    def view(self) -> SessionProcessorView:
        view = mock(SessionProcessorView)
        when(view).process('input', 'output')
        return view

    @fixture
    def app(self, view: SessionProcessorView) -> Application:
        return Application(view=view)

    @patch('sys.argv', ['_', 'input', 'output'])
    def test_raises_on_run(
            self, app: Application, view: SessionProcessorView,
    ) -> None:
        app.run()
