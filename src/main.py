from src.app import Application
from src.loader import PSVLoader
from src.view import SessionProcessorView


def build_application() -> Application:
    loader = PSVLoader()
    view = SessionProcessorView(loader=loader)
    return Application(view=view)


def main() -> None:
    app = build_application()
    app.run()


if __name__ == '__main__':
    main()
