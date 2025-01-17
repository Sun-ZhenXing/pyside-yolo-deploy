# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(600, 500)
        self.gridLayout_2 = QGridLayout(Login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.usernameLineEdit = QLineEdit(Login)
        self.usernameLineEdit.setObjectName("usernameLineEdit")

        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginPushButton = QPushButton(Login)
        self.loginPushButton.setObjectName("loginPushButton")

        self.horizontalLayout.addWidget(self.loginPushButton)

        self.registerPushButton = QPushButton(Login)
        self.registerPushButton.setObjectName("registerPushButton")

        self.horizontalLayout.addWidget(self.registerPushButton)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.passwordLineEdit = QLineEdit(Login)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(Login)
        self.label.setObjectName("label")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.loginPushButton)
        QWidget.setTabOrder(self.loginPushButton, self.registerPushButton)

        self.retranslateUi(Login)
        self.usernameLineEdit.returnPressed.connect(self.passwordLineEdit.setFocus)
        self.passwordLineEdit.returnPressed.connect(self.loginPushButton.click)
        self.loginPushButton.clicked.connect(Login.login)
        self.registerPushButton.clicked.connect(Login.register)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", "\u767b\u5f55", None))
        self.loginPushButton.setText(
            QCoreApplication.translate("Login", "\u767b\u5f55(&L)", None)
        )
        self.registerPushButton.setText(
            QCoreApplication.translate("Login", "\u6ce8\u518c(&R)", None)
        )
        self.label_2.setText(QCoreApplication.translate("Login", "\u5bc6\u7801", None))
        self.label.setText(
            QCoreApplication.translate("Login", "\u7528\u6237\u540d", None)
        )

    # retranslateUi
