# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventanas\CreateUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        CreateUser.setObjectName("CreateUser")
        CreateUser.resize(409, 226)
        self.centralwidget = QtWidgets.QWidget(CreateUser)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 146))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUser = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelUser.setObjectName("labelUser")
        self.verticalLayout.addWidget(self.labelUser)
        self.editUser = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editUser.setObjectName("editUser")
        self.verticalLayout.addWidget(self.editUser)
        self.labelPass = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPass.setObjectName("labelPass")
        self.verticalLayout.addWidget(self.labelPass)
        self.editPass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPass.setObjectName("editPass")
        self.verticalLayout.addWidget(self.editPass)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editPass_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editPass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPass_2.setObjectName("editPass_2")
        self.verticalLayout.addWidget(self.editPass_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 20, 95, 98))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnCrear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnCrear.setObjectName("btnCrear")
        self.verticalLayout_2.addWidget(self.btnCrear)
        self.btnCancel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout_2.addWidget(self.btnCancel)
        self.labelAcceso = QtWidgets.QLabel(self.centralwidget)
        self.labelAcceso.setGeometry(QtCore.QRect(140, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelAcceso.setFont(font)
        self.labelAcceso.setText("")
        self.labelAcceso.setObjectName("labelAcceso")
        CreateUser.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(CreateUser)
        self.statusBar.setObjectName("statusBar")
        CreateUser.setStatusBar(self.statusBar)

        self.retranslateUi(CreateUser)
        QtCore.QMetaObject.connectSlotsByName(CreateUser)

    def retranslateUi(self, CreateUser):
        _translate = QtCore.QCoreApplication.translate
        CreateUser.setWindowTitle(_translate("CreateUser", "Crear Usuario..."))
        self.labelUser.setText(_translate("CreateUser", "Nombre de Usuario"))
        self.editUser.setStatusTip(_translate("CreateUser", "Nombre de Usuario"))
        self.labelPass.setText(_translate("CreateUser", "Contrase??a"))
        self.editPass.setStatusTip(_translate("CreateUser", "Ingrese su Contrase??a"))
        self.label.setText(_translate("CreateUser", "Repita su contrase??a"))
        self.editPass_2.setStatusTip(_translate("CreateUser", "Ingrese su Contrase??a"))
        self.btnCrear.setText(_translate("CreateUser", "Crear Usuario"))
        self.btnCancel.setText(_translate("CreateUser", "Cancelar"))
