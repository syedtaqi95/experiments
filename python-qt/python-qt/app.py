import sys
from os import path
from typing import Type

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, Slot, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        currentDirectory = path.dirname(path.realpath(__file__))

        buttonAction = QAction(
            QIcon(path.join("/", currentDirectory, "bug.png")), "The Button", self
        )
        buttonAction.setStatusTip("This is The Button")
        buttonAction.triggered.connect(self.onToolbarButtonClick)
        buttonAction.setCheckable(True)
        toolbar.addAction(buttonAction)

        toolbar.addSeparator()

        buttonAction2 = QAction(
            QIcon(path.join("/", currentDirectory, "bug.png")), "Button 2", self
        )
        buttonAction2.setStatusTip("This is Button 2")
        buttonAction2.triggered.connect(self.onToolbarButtonClick)
        buttonAction2.setCheckable(True)
        toolbar.addAction(buttonAction2)

        toolbar.addWidget(QLabel("The Label"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onToolbarButtonClick(self, s: Type[Slot]):
        print(f"click {s}")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()
