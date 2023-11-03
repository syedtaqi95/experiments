import sys
from time import localtime, strftime
from typing import Self

from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class Backend(QObject):
    hms = Signal(int, int, int, arguments=["hours", "minutes", "seconds"])

    def __init__(self: Self) -> None:
        super().__init__()

        # Define timer
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start()

    def updateTime(self: Self) -> None:
        # Pass the current time to QML
        local_time = localtime()
        self.hms.emit(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)


def main() -> None:
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load("qtquick_demo/main.qml")

    backend = Backend()
    engine.rootObjects()[0].setProperty("backend", backend)
    backend.updateTime()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
