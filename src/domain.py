from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta
from typing import Dict, Generator
from typing import List


@dataclass
class Statement:
    home_no: int
    channel: int
    start_time: datetime
    activity: str


StatementGenerator = Generator[Statement, None, None]
StatementsByHomeNo = Dict[int, List[Statement]]


@dataclass
class Session:
    home_no: int
    channel: int
    start_time: datetime
    activity: str
    end_time: datetime
    duration: timedelta


SessionGenerator = Generator[Session, None, None]
