import sys

from PySide6.QtWidgets import QApplication

from app.views.main import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    sys.exit(exit_code)
