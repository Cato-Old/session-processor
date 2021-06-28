from src.domain import StatementGenerator
from src.domain import StatementsByHomeNo


class StatementGrouper:
    @staticmethod
    def group(statements: StatementGenerator) -> StatementsByHomeNo:
        grouped = {}
        for statement in statements:
            try:
                grouped[statement.home_no].append(statement)
            except KeyError:
                grouped[statement.home_no] = [statement]
        return grouped
