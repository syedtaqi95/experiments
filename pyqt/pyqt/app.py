# Only needed for access to command line arguments
import sys
from os import path
import typing

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, pyqtBoundSignal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        iconPath = path.join("/", path.dirname(path.realpath(__file__)), "bug.png")

        buttonAction = QAction(
            QIcon(iconPath),
            "The Button",
            self,
        )
        buttonAction.setStatusTip("This is The Button")
        buttonAction.triggered.connect(self.handleButtonClick)
        buttonAction.setCheckable(True)
        toolbar.addAction(buttonAction)

        self.setStatusBar(QStatusBar(self))

    def handleButtonClick(
        self, s: typing.Union[typing.Callable[..., None], pyqtBoundSignal]
    ):
        print(f"click {s}")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
