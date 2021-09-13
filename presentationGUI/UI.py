from business.admin import Admin,Buyer,Depositor,Collector,AccountBuilder,UserBuilder
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore
from decimal import Decimal
import getpass
from ventanas.Login import Ui_Loggeo
from ventanas.CreateUserDialog import Ui_CreateUserDialog
from ventanas.MenuCuentas import Ui_CountsWindow
from ventanas.CrearCuentaDialog import Ui_CrearCuentaDialog
from ventanas.DepositDialog import Ui_DepositDialog
from ventanas.TradeDialog import Ui_TradeDialog


class Logger_Window(Ui_Loggeo,QMainWindow):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.admin=admin
        self.btnEnter.clicked.connect(lambda x:self.enter())
        self.btnCancel.clicked.connect(lambda x:self.cancel())
        self.editPass.returnPressed.connect(lambda :self.enter())
        self.btnCrear.clicked.connect(lambda x:self.create())


    def enter(self):

        def success(self):
            siguienteWindow=MenuCuentasWindow(self.admin)
            siguienteWindow.show()
            self.close()
        def noUser(self):
            self.labelAcceso.setText("Rechazado")
        def noPass(self):
            self.labelAcceso.setText("Rechazado")

        actionDict={
            True:success,
            False:noPass,
            None:noUser
        }
        name=self.editUser.text()
        pwd=self.editPass.text()           
        result = self.admin.CheckValidate(name, pwd)
        actionDict[result](self)
    
    def cancel(self):
        self.close()

    def create(self):
        siguienteWindow=CreateUserWindow(self.admin)
        siguienteWindow.exec_()
        
class CreateUserWindow(Ui_CreateUserDialog,QDialog):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin
        self.btnCrear.clicked.connect(lambda x:self.enter())
        
    def enter(self):
        def success(self):
            self.userBuilder.Build(self.admin)
            print('Exito')
            self.close()
        def AlreadyExist(self):
            print('Ya existe el usuario')
            self.close()
        def PassNotMatch(self):
            print('Los pass no coinciden')
            self.close()

        resultDict={
            'TrueTrue':success,
            'FalseTrue':AlreadyExist,
            'TrueFalse':PassNotMatch,
            'FalseFalse':AlreadyExist
        }


        name=self.editUser.text()
        pwd=self.editPass.text()
        pwd2=self.editPass_2.text()           
        rv=""
        self.userBuilder=UserBuilder(name,pwd)
        rv+=str(self.userBuilder.validateUser(self.admin))
        rv+=str(self.userBuilder.validatePwd(pwd2))
        resultDict[rv](self)

class MenuCuentasWindow(Ui_CountsWindow,QMainWindow):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin 
        self.tablaCuentas.setGeometry(QtCore.QRect(10, 10, 280, 450))
        self.actionCrearCuenta.triggered.connect(lambda x:self.CreateAccount())
        self.actionOperar.triggered.connect(lambda x:self.Operate())
        self.actionDepositar.triggered.connect(lambda x:self.Deposit())
        self.FillAccounts()

    def FillAccounts(self):
        def success(self):
            self.tablaCuentas.setRowCount(0)
            for count in self.result:
                row=self.tablaCuentas.rowCount()
                self.tablaCuentas.insertRow(row)
                currency = QTableWidgetItem(str(count['currency']))
                currency.setFlags( QtCore.Qt.ItemIsEnabled)
                amount= QTableWidgetItem(str(count['amount']))
                amount.setFlags( QtCore.Qt.ItemIsEnabled)
                self.tablaCuentas.setItem(row,0,currency)
                self.tablaCuentas.setItem(row,1,amount)
        def noAccounts(self):
            pass

        actionDict={
            True:success,
            False:noAccounts
        }
        self.result = self.admin.CheckAccount()
        actionDict[bool(self.result)](self)

    def CreateAccount(self):
        actionDict={
            1:lambda:self.statusBar.showMessage('Cuenta creada con exito!',2000),
            -1:lambda:self.statusBar.showMessage('La cuenta ya existe!',2000),
            -2:lambda:self.statusBar.showMessage('El tipo de cuenta no existe!',2000),
            0:lambda:self.statusBar.showMessage('Cancelado',2000),
        }
        self.Dialog=CrearCuentaDialog(self.admin)
        result=self.Dialog.exec_()
        actionDict[result]()
        self.FillAccounts()

    def Deposit(self):
        actionDict={
            1:lambda:self.statusBar.showMessage('Deposito Exitoso!',2000),
            -1:lambda:self.statusBar.showMessage('Pago Rechazado',2000),
            0:lambda:self.statusBar.showMessage('Cancelado',2000),
            -3:lambda:self.statusBar.showMessage('ERROR-3',2000),
            -2:lambda:self.statusBar.showMessage('ERROR-2',2000),
            -4:lambda:self.statusBar.showMessage('El monto no es un numero!',2000)
        }
        self.Dialog=DepositDialog(self.admin)
        result=self.Dialog.exec_()
        actionDict[result]()
        self.FillAccounts()

    def Operate(self):
        actionDict={
            1:lambda:self.statusBar.showMessage('Operacion Exitosa!',2000),
            -1:lambda:self.statusBar.showMessage('La cuenta origen y destino son la misma!',2000),
            0:lambda:self.statusBar.showMessage('Cancelado',2000),
            -3:lambda:self.statusBar.showMessage('Seleccione Debito o Compra',2000),
            -2:lambda:self.statusBar.showMessage('No hay fondos suficientes',2000),
            -4:lambda:self.statusBar.showMessage('El monto no es un numero!',2000)
        }
        self.dialog=TradeDialog(self.admin)
        result=self.dialog.exec_()
        actionDict[result]()
        self.FillAccounts()

class CrearCuentaDialog(Ui_CrearCuentaDialog,QDialog):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin
        symbols=admin.CurrencyQuery()
        for currency in symbols.keys():        
            self.comboBox.addItem(f'{currency}={symbols[currency]}')
        self.btnAccept.clicked.connect(lambda:self.enter())
        self.btnCancel.clicked.connect(lambda:self.close())
        

    def enter(self):
        def success(self):
            MyAccountBuilder.Build(self.admin)
            self.done(1)
        def alreadyExist(self):
            self.done(-1)
        def noCurrency(self):
            self.done(-2)

        actionDict={
            True:success,
            False:alreadyExist,
            None:noCurrency
        }
        MyAccountBuilder=AccountBuilder(self.comboBox.currentText().split('=')[0])
        res=MyAccountBuilder.prepare(self.admin)
        actionDict[res](self)

class DepositDialog(Ui_DepositDialog,QDialog):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin
        self.btnAccept.clicked.connect(lambda x:self.enter())
        self.btnCancel.clicked.connect(lambda x:self.done(0))
    def enter(self):
        resultDict={
            'TrueTrue':1,
            'FalseTrue':-3,
            'TrueFalse':-1,
            'FalseFalse':-2
        }
        rv=""
        try:
            cnt=Decimal(self.depositEdit.text())
            MyDepositor=Depositor(cnt)
            MyCollector=Collector()
            MyDepositor.prepare(self.admin)
            #preguntar si o no
            rv+=str(MyDepositor.validate(self.admin))
            rv+=str(MyCollector.validate()) #aqui realizaria el cobro
            self.done(resultDict[rv])
        except:
            self.done(-4)

class TradeDialog(Ui_TradeDialog,QDialog):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin
        self.btnAccept.clicked.connect(lambda x:self.enter())
        result=self.admin.CheckAccount()
        for count in result:       
            self.orgCrrncy.addItem(f'{count["currency"]}')
            self.dstCrrncy.addItem(f'{count["currency"]}')
        self.btnComprar.setChecked(True)
        self.btnCancel.clicked.connect(lambda x:self.done(0))
    def enter(self):
        def success(self):
            self.MyBuyer.validate(self.admin,self.res['bal_org'],self.res['bal_dst'])
            self.done(1)
        def noMoney(self):
            self.done(-2)
        actionDict={
            'OK':success,
            'NOT OK':noMoney
        }
        org = self.orgCrrncy.currentText()
        dst = self.dstCrrncy.currentText()
        if org==dst:
            self.done(-1)
        else:
            try:
                cnt=Decimal(self.buyerEdit.text())
                if self.btnComprar.isChecked():
                    op='BUY'
                elif self.btnDebitar.isChecked():
                    op='DEBIT'
                else:
                    self.done(-3)
                self.MyBuyer=Buyer(operation=op,org=org,dst=dst,cnt=cnt)
                self.res=self.MyBuyer.prepare(self.admin)
                actionDict[self.res['status']](self)
            except:
                self.done(-4)
            
class App(object):

    """Clase Base de la Aplicacion, usada para iniciarla"""
    
    def main():
    
        """Metodo que inicia la aplicacion y 
        realiza el bucle de seleccion de opciones"""

        app=QApplication([])
        admin = Admin()
        myLogger=Logger_Window(admin)
        myLogger.show()
        app.exec_()
