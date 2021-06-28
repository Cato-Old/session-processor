from src.app import Application
from src.controller.controller import SessionProcessorController
from src.controller.creator import SessionCreator
from src.controller.grouper import StatementGrouper
from src.controller.sorter import StatementSorter
from src.dumper import PSVDumper
from src.loader import PSVLoader
from src.view import SessionProcessorView


def build_application() -> Application:
    loader = PSVLoader()
    controller = build_controller()
    dumper = PSVDumper()
    view = SessionProcessorView(
        loader=loader, controller=controller, dumper=dumper,
    )
    return Application(view=view)


def build_controller() -> SessionProcessorController:
    grouper = StatementGrouper()
    sorter = StatementSorter()
    creator = SessionCreator()
    return SessionProcessorController(
        grouper=grouper, sorter=sorter, creator=creator,
    )


def main() -> None:
    app = build_application()
    app.run()


if __name__ == '__main__':
    main()
