import filecmp
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
    def input_data(self, project_path: str) -> str:
        return join(project_path, 'tests', 'data', 'input.psv')

    @fixture
    def output_data(self, project_path: str) -> str:
        return join(project_path, 'tests', 'data', 'output.psv')

    @fixture
    def output_example(self, project_path: str) -> str:
        return join(project_path, 'tests', 'data', 'output_example.psv')

    @fixture
    def env(self, project_path: str) -> dict:
        env = os.environ
        env.update({'PYTHONPATH': project_path})
        return env

    def test_is_app_running(
            self, path: str, env: dict, input_data: str, output_data: str,
    ) -> None:
        arguments = ['python', path, input_data, output_data]
        result = run(arguments, env=env)
        assert result.returncode == 0

    def test_produces_expected_output(
            self,
            path: str,
            env: dict,
            input_data: str,
            output_data: str,
            output_example: str,
    ) -> None:
        arguments = ['python', path, input_data, output_data]
        run(arguments, env=env)
        assert filecmp.cmp(output_example, output_data)
