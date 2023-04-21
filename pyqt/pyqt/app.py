# Only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QTabWidget,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


class Color(QWidget):
    def __init__(self, color: Qt.GlobalColor | str) -> None:
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
