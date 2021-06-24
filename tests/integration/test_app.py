from os.path import dirname
from os.path import join
from subprocess import run

from pytest import fixture


class TestApp:
    @fixture
    def path(self) -> str:
        return join(dirname(__file__), '..', '..', 'src', 'app')

    def test_is_app_running(self, path: str) -> None:
        arguments = ['python', path]
        result = run(arguments)
        assert result.returncode == 0
