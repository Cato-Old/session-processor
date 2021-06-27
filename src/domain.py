from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta


@dataclass
class Statement:
    home_no: int
    channel: int
    start_time: datetime
    activity: str


@dataclass
class Session:
    home_no: int
    channel: int
    start_time: datetime
    activity: str
    end_time: datetime
    duration: timedelta
