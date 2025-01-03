import sys

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from app.config import GlobalConfig
from app.views.main import MainWindow


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    if exit_code == GlobalConfig.RESTART_CODE:
        QProcess.startDetached(app.applicationFilePath(), sys.argv)
        sys.exit(GlobalConfig.EXIT_CODE)
    sys.exit(exit_code)
