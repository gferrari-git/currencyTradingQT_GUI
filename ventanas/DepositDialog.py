# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventanas\DepositDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DepositDialog(object):
    def setupUi(self, DepositDialog):
        DepositDialog.setObjectName("DepositDialog")
        DepositDialog.resize(369, 182)
        self.horizontalLayoutWidget = QtWidgets.QWidget(DepositDialog)
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
        self.label = QtWidgets.QLabel(DepositDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 227, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.depositEdit = QtWidgets.QLineEdit(DepositDialog)
        self.depositEdit.setGeometry(QtCore.QRect(20, 80, 131, 22))
        self.depositEdit.setText("")
        self.depositEdit.setMaxLength(10)
        self.depositEdit.setObjectName("depositEdit")

        self.retranslateUi(DepositDialog)
        QtCore.QMetaObject.connectSlotsByName(DepositDialog)

    def retranslateUi(self, DepositDialog):
        _translate = QtCore.QCoreApplication.translate
        DepositDialog.setWindowTitle(_translate("DepositDialog", "Deposito"))
        self.btnAccept.setText(_translate("DepositDialog", "Aceptar"))
        self.btnCancel.setText(_translate("DepositDialog", "Cancelar"))
        self.label.setText(_translate("DepositDialog", "Cantidad de Pesos a Depositar"))
        self.depositEdit.setPlaceholderText(_translate("DepositDialog", "ARS $"))