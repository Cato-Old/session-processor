import datetime
from typing import List

from factory import Factory, LazyAttribute
from factory.fuzzy import FuzzyInteger
from factory.fuzzy import FuzzyNaiveDateTime
from factory.fuzzy import FuzzyText
from pytest import fixture

from src.controller.creator import SessionCreator
from src.domain import Session
from src.domain import StatementsByHomeNo

from tests.unit.test_loader import StatementFactory


class SessionFactory(Factory):
    class Meta:
        model = Session

    home_no = FuzzyInteger(0)
    channel = FuzzyInteger(0)
    start_time = FuzzyNaiveDateTime(datetime.datetime(2021, 1, 1))
    activity = FuzzyText()
    end_time = LazyAttribute(lambda o: FuzzyNaiveDateTime(o.start_time).fuzz())
    duration = LazyAttribute(lambda o: o.end_time-o.start_time)


class TestSessionCreator:
    @fixture
    def creator(self) -> SessionCreator:
        return SessionCreator()

    @fixture
    def sorted_statements(self) -> StatementsByHomeNo:
        home_numbers = (FuzzyInteger(0).fuzz() for _ in range(10))
        statements = {
            no: StatementFactory.build_batch(3, home_no=no)
            for no in home_numbers
        }
        for statement in statements:
            statements[statement].sort(key=lambda s: s.start_time)
        return statements

    @fixture
    def expected(self, sorted_statements: StatementsByHomeNo) -> List[Session]:
        sessions = []
        for _, statements in sorted_statements.items():
            for start, end in zip(statements, [*statements[1:], None]):
                end_time = (
                        end.start_time - datetime.timedelta(seconds=1)
                        if end else datetime.datetime(
                            year=start.start_time.year,
                            month=start.start_time.month,
                            day=start.start_time.day,
                            hour=23,
                            minute=59,
                            second=59,
                        )
                )
                duration = end_time - start.start_time
                session = Session(
                    home_no=start.home_no,
                    channel=start.channel,
                    start_time=start.start_time,
                    activity=start.activity,
                    end_time=end_time,
                    duration=duration,
                )
                sessions.append(session)
        return sessions

    def test_creates_sessions(
            self,
            creator: SessionCreator,
            sorted_statements: StatementsByHomeNo,
            expected: List[Session],
    ) -> None:
        actual = creator.create(sorted_statements)
        assert list(actual) == expected
