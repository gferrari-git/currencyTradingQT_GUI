# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventanas\CrearCuentaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CrearCuentaDialog(object):
    def setupUi(self, CrearCuentaDialog):
        CrearCuentaDialog.setObjectName("CrearCuentaDialog")
        CrearCuentaDialog.resize(369, 182)
        self.verticalLayoutWidget = QtWidgets.QWidget(CrearCuentaDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(CrearCuentaDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(CrearCuentaDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 130, 194, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAccept = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)

        self.retranslateUi(CrearCuentaDialog)
        QtCore.QMetaObject.connectSlotsByName(CrearCuentaDialog)

    def retranslateUi(self, CrearCuentaDialog):
        _translate = QtCore.QCoreApplication.translate
        CrearCuentaDialog.setWindowTitle(_translate("CrearCuentaDialog", "CrearCuenta"))
        self.label.setText(_translate("CrearCuentaDialog", "Cuenta a crear"))
        self.btnAccept.setText(_translate("CrearCuentaDialog", "Aceptar"))
        self.btnCancel.setText(_translate("CrearCuentaDialog", "Cancelar"))
