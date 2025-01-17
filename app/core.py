import sys

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet

from app.config import GlobalConfig
from app.views.login import LoginWindow
from app.views.main import MainWindow
from app.views.register import RegisterWindow


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")
    windows_map: dict[str, QWidget] = {}
    window = MainWindow(windows_map)
    windows_map["main"] = window
    login = LoginWindow(windows_map)
    windows_map["login"] = login
    register = RegisterWindow(windows_map)
    windows_map["register"] = register
    login.show()
    exit_code = app.exec()
    if exit_code == GlobalConfig.RESTART_CODE:
        QProcess.startDetached(app.applicationFilePath(), sys.argv)
        sys.exit(GlobalConfig.EXIT_CODE)
    sys.exit(exit_code)
