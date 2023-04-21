# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout
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

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))
        layout1.addLayout(layout2)
        
        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))
        layout1.addLayout(layout3)

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
