import datetime
import os
from csv import DictWriter
from tempfile import NamedTemporaryFile
from typing import List
from typing import Tuple

from factory import Factory
from factory.fuzzy import FuzzyInteger
from factory.fuzzy import FuzzyNaiveDateTime
from factory.fuzzy import FuzzyText
from pytest import fixture

from src.domain import Statement
from src.loader import PSVLoader, SplitDate

InputValue = Tuple[int, int, int, str]


class StatementFactory(Factory):
    class Meta:
        model = Statement

    home_no = FuzzyInteger(0)
    channel = FuzzyInteger(0)
    start_time = FuzzyNaiveDateTime(datetime.datetime(2021, 1, 1))
    activity = FuzzyText()


class TestPSVLoader:
    @fixture
    def input_values(self) -> List[InputValue]:
        return [
            (1234, 101, 20200101180000, 'Live'),
            (1234, 102, 20200101183000, 'Live'),
            (45678, 103, 20200101190000, 'PlayBack'),
            (45678, 104, 20200101193000, 'Live'),
        ]

    @fixture
    def psv_file(self, input_values: List[InputValue]) -> NamedTemporaryFile:
        fieldnames = ['HomeNo', 'Channel', 'Starttime', 'Activity']
        rowdicts = [
            {name: value for name, value in zip(fieldnames, v)}
            for v in input_values
        ]
        with NamedTemporaryFile(mode='w', newline='', delete=False) as ntf:
            writer = DictWriter(ntf, fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerows(rowdicts)
        yield ntf
        os.remove(ntf.name)

    @fixture
    def loader(self) -> PSVLoader:
        return PSVLoader()

    @fixture
    def path(self, psv_file: NamedTemporaryFile) -> str:
        return psv_file.name

    @fixture
    def expected(self, input_values: List[InputValue]) -> List[Statement]:
        return [
            StatementFactory(
                home_no=v[0],
                channel=v[1],
                start_time=datetime.datetime(*self.split_raw_date(v[2])),
                activity=v[3],
            ) for v in input_values
        ]

    def test_raises_on_load(
            self, loader: PSVLoader, path: str, expected: List[Statement],
    ) -> None:
        actual = loader.load(path)
        assert list(actual) == expected

    @staticmethod
    def split_raw_date(raw_date: int) -> SplitDate:
        string_date = str(raw_date)
        return(
            int(string_date[0:4]),
            int(string_date[4:6]),
            int(string_date[6:8]),
            int(string_date[8:10]),
            int(string_date[10:12]),
            int(string_date[12:14]),
        )
