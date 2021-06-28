from pytest import fixture
from pytest import raises

from src.domain import SessionGenerator
from src.dumper import PSVDumper

from tests.unit.controller.test_creator import SessionFactory


class TestPSVDumper:
    @fixture
    def sessions(self) -> SessionGenerator:
        return (s for s in SessionFactory.build_batch(10))

    @fixture
    def dumper(self) -> PSVDumper:
        return PSVDumper()

    def test_raises_on_dump(
            self, dumper: PSVDumper, sessions: SessionGenerator,
    ) -> None:
        with raises(NotImplementedError):
            dumper.dump(sessions)

