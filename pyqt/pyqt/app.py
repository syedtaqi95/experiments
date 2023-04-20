# Only needed for access to command line arguments
import sys
from typing import Type

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    QListWidget,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
)
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Widgets App")

        widget = QLabel()
        widget.setPixmap(QPixmap("test-image.png"))
        widget.setScaledContents(True)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
