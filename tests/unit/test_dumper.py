import os
from csv import DictWriter
from tempfile import NamedTemporaryFile

from pytest import fixture

from src.domain import SessionGenerator
from src.dumper import PSVDumper

from tests.unit.controller.test_creator import SessionFactory


class TestPSVDumper:
    @fixture
    def dumper(self) -> PSVDumper:
        return PSVDumper()

    def test_can_instantiate(self):
        pass
