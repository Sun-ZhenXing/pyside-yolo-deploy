import sqlite3
from hashlib import sha256

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QWidget

from app.widgets.login_ui import Ui_Login


class LoginWindow(QWidget):
    def __init__(
        self,
        windows_map: dict[str, QWidget] | None = None,
        parent: QWidget | None = None,
    ) -> None:
        self._windows_map = windows_map if windows_map is not None else {}
        super().__init__(parent)
        self._ui = Ui_Login()
        self._ui.setupUi(self)

    @Slot()
    def login(self) -> None:
        # TODO: login
        username = self._ui.usernameLineEdit.text()
        password = self._ui.passwordLineEdit.text()
        # 表单校验
        if username == "" or password == "":
            QMessageBox.warning(
                self,
                "错误",
                "用户名密码不能为空！",
                QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Ok,
            )
            return
        if len(username) < 3 or len(password) < 6:
            QMessageBox.warning(
                self,
                "错误",
                "用户名长度不能小于3位，密码长度不能小于6位！",
                QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Ok,
            )
            return
        # 连接数据库
        conn = sqlite3.connect("./data/database.db")
        if conn is None:
            print("Error: cannot connect to database")
            return
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE username=?",
            (username,),
        )
        values = cursor.fetchall()
        conn.commit()
        if sha256(password.encode()).hexdigest() != values[0][2]:
            QMessageBox.warning(
                self,
                "错误",
                "密码不正确！",
                QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Ok,
            )
            return
        main_window = self._windows_map.get("main")
        if main_window is None:
            return None
        self.close()
        main_window.show()

    @Slot()
    def register(self) -> None:
        register_window = self._windows_map.get("register")
        if register_window is None:
            return None
        self.close()
        register_window.show()
