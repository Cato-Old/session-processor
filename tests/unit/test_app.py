from pytest import fixture
from pytest import raises

from src.app import Application


class TestApplication:
    @fixture
    def app(self) -> Application:
        return Application()

    def test_raises_on_run(self, app: Application) -> None:
        with raises(NotImplementedError):
            app.run()
