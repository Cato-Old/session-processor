from src.app import Application
from src.view import SessionProcessorView


def build_application() -> Application:
    view = SessionProcessorView()
    return Application(view=view)


def main() -> None:
    app = build_application()
    app.run()


if __name__ == '__main__':
    main()
