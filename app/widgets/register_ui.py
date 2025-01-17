# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName("Register")
        Register.resize(600, 500)
        self.gridLayout_2 = QGridLayout(Register)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(Register)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Register)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QLabel(Register)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(Register)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.emailLineEdit = QLineEdit(Register)
        self.emailLineEdit.setObjectName("emailLineEdit")

        self.gridLayout.addWidget(self.emailLineEdit, 3, 1, 1, 1)

        self.label = QLabel(Register)
        self.label.setObjectName("label")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.usernameLineEdit = QLineEdit(Register)
        self.usernameLineEdit.setObjectName("usernameLineEdit")

        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)

        self.passwordLineEdit = QLineEdit(Register)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 2, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        QWidget.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.emailLineEdit)
        QWidget.setTabOrder(self.emailLineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)

        self.retranslateUi(Register)
        self.usernameLineEdit.returnPressed.connect(self.passwordLineEdit.setFocus)
        self.passwordLineEdit.returnPressed.connect(self.emailLineEdit.setFocus)
        self.emailLineEdit.returnPressed.connect(self.pushButton.click)
        self.pushButton.clicked.connect(Register.register)
        self.pushButton_2.clicked.connect(Register.cancel)

        QMetaObject.connectSlotsByName(Register)

    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(
            QCoreApplication.translate("Register", "register", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("Register", "\u6ce8\u518c", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Register", "\u53d6\u6d88", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Register", "\u5bc6\u7801", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Register", "\u90ae\u7bb1", None)
        )
        self.label.setText(
            QCoreApplication.translate("Register", "\u7528\u6237\u540d", None)
        )

    # retranslateUi
