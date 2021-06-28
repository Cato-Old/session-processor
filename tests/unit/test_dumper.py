from pytest import fixture

from src.dumper import PSVDumper


class TestPSVDumper:
    @fixture
    def dumper(self) -> PSVDumper:
        return PSVDumper()

    def test_can_instantiate(self):
        pass
