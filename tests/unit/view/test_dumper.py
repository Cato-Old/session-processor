import filecmp
import os
from csv import DictWriter
from tempfile import NamedTemporaryFile
from typing import List

from pytest import fixture

from src.domain import SessionGenerator, Session
from src.view.dumper import PSVDumper

from tests.unit.controller.test_creator import SessionFactory


class TestPSVDumper:
    @fixture
    def session_values(self) -> List[Session]:
        return SessionFactory.build_batch(10)

    @fixture
    def sessions(self, session_values) -> SessionGenerator:
        return (s for s in session_values)

    @fixture
    def dumper(self) -> PSVDumper:
        return PSVDumper()

    @fixture
    def expected(self, session_values: List[Session]) -> str:
        fieldnames = [
            'HomeNo',
            'Channel',
            'Starttime',
            'Activity',
            'Endtime',
            'Duration',
        ]
        rowdicts = [
            {
                'HomeNo': session.home_no,
                'Channel': session.channel,
                'Starttime': session.start_time.strftime('%Y%m%d%H%M%S'),
                'Activity': session.activity,
                'Endtime': session.end_time.strftime('%Y%m%d%H%M%S'),
                'Duration': int(session.duration.total_seconds()),
            } for session in session_values
        ]
        with NamedTemporaryFile(mode='w', newline='', delete=False) as ntf:
            writer = DictWriter(ntf, fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerows(rowdicts)
        yield ntf.name
        os.remove(ntf.name)

    @fixture
    def path(self) -> str:
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'output_example.psv')
        yield path
        os.remove(path)

    def test_dumps_sessions_to_psv_file(
            self,
            dumper: PSVDumper,
            sessions: SessionGenerator,
            expected: NamedTemporaryFile,
            path: str,
    ) -> None:
        dumper.dump(sessions, path)
        assert filecmp.cmp(expected, path)
