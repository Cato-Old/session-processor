from src.domain import StatementsByHomeNo


class StatementSorter:
    @staticmethod
    def sort(grouped_statement: StatementsByHomeNo) -> StatementsByHomeNo:
        for key in grouped_statement:
            grouped_statement[key].sort(key=lambda s: s.start_time)
        return grouped_statement
