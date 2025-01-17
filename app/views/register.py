import re
import sqlite3
from hashlib import sha256

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QWidget

from app.widgets.register_ui import Ui_Register


class RegisterWindow(QWidget):
    def __init__(
        self,
        windows_map: dict[str, QWidget] | None = None,
        parent: QWidget | None = None,
    ) -> None:
        self._windows_map = windows_map if windows_map is not None else {}
        super().__init__(parent)
        self._ui = Ui_Register()
        self._ui.setupUi(self)

    @Slot()
    def register(self) -> None:
        # 获取窗口username password email
        username = self._ui.usernameLineEdit.text()
        password = self._ui.passwordLineEdit.text()
        email = self._ui.emailLineEdit.text()
        # 表单校验
        if username == "" or password == "" or email == "":
            QMessageBox.warning(
                self,
                "错误",
                "用户名密码或邮箱不能为空！",
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
        if (
            re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email)
            is None
        ):
            QMessageBox.warning(
                self,
                "错误",
                "请输入正确的邮箱格式！",
                QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Ok,
            )
        # 连接数据库
        conn = sqlite3.connect("./data/database.db")
        if conn is None:
            print("Error: cannot connect to database")
            return
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user (username, password,email) VALUES (?, ?, ?)",
            (username, sha256(password.encode()).hexdigest(), email),
        )
        conn.commit()
        print("Registering...")
        # 跳转登录窗口
        login_window = self._windows_map.get("login")
        if login_window is None:
            return None
        self.close()
        login_window.show()

    @Slot()
    def cancel(self) -> None:
        # 关闭程序
        self.close()
