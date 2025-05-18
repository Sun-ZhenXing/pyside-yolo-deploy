import sys

from PySide6.QtWidgets import QApplication

# from qt_material import apply_stylesheet
from app.views.main import MainWindow


def main():
    app = QApplication(sys.argv)
    # apply_stylesheet(app, theme="dark_teal.xml")
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    sys.exit(exit_code)
