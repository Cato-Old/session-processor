from abc import ABC
from abc import abstractmethod
from csv import DictWriter

from src.domain import SessionGenerator


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
            {
                'HomeNo': session.home_no,
                'Channel': session.channel,
                'Starttime': session.start_time.strftime('%Y%m%d%H%M%S'),
                'Activity': session.activity,
                'Endtime': session.end_time.strftime('%Y%m%d%H%M%S'),
                'Duration': session.duration.total_seconds(),
            } for session in sessions
        ]
        with open(path, mode='w', newline='') as f:
            writer = DictWriter(f, fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerows(rowdicts)
