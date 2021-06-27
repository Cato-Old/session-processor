from datetime import time, timedelta, datetime
from typing import Dict
from typing import Generator
from typing import List

from src.domain import Statement
from src.domain import Session


class SessionCreator:
    END_OF_DAY = time(hour=23, minute=59, second=59)

    def create(
            self, sorted_statements: Dict[int, List[Statement]],
    ) -> Generator[Session, None, None]:
        for _, statements in sorted_statements.items():
            shifted = [*statements[1:], None]
            for start, end in zip(statements, shifted):
                end_time = (
                    end.start_time - timedelta(seconds=1) if end
                    else datetime(
                        year=start.start_time.year,
                        month=start.start_time.month,
                        day=start.start_time.day,
                        hour=self.END_OF_DAY.hour,
                        minute=self.END_OF_DAY.minute,
                        second=self.END_OF_DAY.second,
                    )
                )
                duration = end_time-start.start_time
                yield Session(
                    home_no=start.home_no,
                    channel=start.channel,
                    start_time=start.start_time,
                    activity=start.activity,
                    end_time=end_time,
                    duration=duration,
                )
