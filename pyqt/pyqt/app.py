# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QStackedLayout
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

        layout = QStackedLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
