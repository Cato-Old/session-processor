from abc import ABC
from abc import abstractmethod
from csv import DictWriter
from typing import Dict, Union

from src.domain import SessionGenerator, Session

DumpedSession = Dict[str, Union[int, str,]]


class Dumper(ABC):
    @abstractmethod
    def dump(self, sessions: SessionGenerator, path: str) -> None:
        raise NotImplementedError


class PSVDumper(Dumper):
    def dump(self, sessions: SessionGenerator, path: str) -> None:
        fieldnames = [
            'HomeNo',
            'Channel',
            'Starttime',
            'Activity',
            'Endtime',
            'Duration',
        ]
        rowdicts = [
            self._dump_session(session) for session in sessions
        ]
        with open(path, mode='w', newline='') as f:
            writer = DictWriter(f, fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerows(rowdicts)

    @staticmethod
    def _dump_session(session: Session) -> DumpedSession:
        return {
                'HomeNo': session.home_no,
                'Channel': session.channel,
                'Starttime': session.start_time.strftime('%Y%m%d%H%M%S'),
                'Activity': session.activity,
                'Endtime': session.end_time.strftime('%Y%m%d%H%M%S'),
                'Duration': int(session.duration.total_seconds()),
        }
