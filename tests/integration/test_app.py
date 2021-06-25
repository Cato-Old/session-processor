import os
from os.path import dirname
from os.path import join
from subprocess import run

from pytest import fixture


class TestApp:
    @fixture
    def project_path(self) -> str:
        return join(dirname(__file__), '..', '..')

    @fixture
    def path(self, project_path: str) -> str:
        return join(project_path, 'src', 'main.py')

    @fixture
    def env(self, project_path: str) -> dict:
        env = os.environ
        env.update({'PYTHONPATH': project_path})
        return env

    def test_is_app_running(self, path: str, env: dict) -> None:
        arguments = ['python', path]
        result = run(arguments, env=env)
        assert result.returncode == 1
