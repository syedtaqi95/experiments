# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


# Qt.GlobalColor._member_names_
class Color(QWidget):
    def __init__(self, color: Qt.GlobalColor | str) -> None:
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stackLayout = QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(self.stackLayout)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        buttonLayout.addWidget(btn)
        self.stackLayout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        buttonLayout.addWidget(btn)
        self.stackLayout.addWidget(Color("green"))

        btn = QPushButton("blue")
        btn.pressed.connect(self.activate_tab_3)
        buttonLayout.addWidget(btn)
        self.stackLayout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stackLayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stackLayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stackLayout.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
