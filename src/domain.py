from dataclasses import dataclass
from datetime import datetime


@dataclass
class Statement:
    home_no: int
    channel: int
    start_time: datetime
    activity: str
