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
        }
        self.Dialog=DepositDialog(self.admin)
        result=self.Dialog.exec_()
        actionDict[result]()
        self.FillAccounts()

    def Operate(self):
        self.dialog=TradeDialog(self.admin)
        self.dialog.exec_()
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
        MyAccountBuilder=AccountBuilder(self.comboBox.currentText())
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
        cnt=Decimal(self.depositEdit.text())
        MyDepositor=Depositor(cnt)
        MyCollector=Collector()
        MyDepositor.prepare(self.admin)
        #preguntar si o no
        rv+=str(MyDepositor.validate(self.admin))
        rv+=str(MyCollector.validate()) #aqui realizaria el cobro
        self.done(resultDict[rv])

class TradeDialog(Ui_TradeDialog,QDialog):
    def __init__(self,admin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)    
        self.admin=admin
        self.btnAccept.clicked.connect(lambda x:self.enter())
    def enter(self):
        pass

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



    """Clase Encargada de mostrar opciones en 
    la pantalla y mostrar resultados"""
    
    def __init__(self,admin):
        self.admin=admin

    def ShowLogin(self):

        """Metodo que toma los datos del login (user y pwd) e 
        informa la validacion del mismo"""
        
        name=input("User:")
        pwd = getpass.getpass('Password:')
        result = self.admin.CheckValidate(name, pwd)
        if result==True:
            print ('Acceso correcto')
        elif result == False:
            print ('Password y/o usuario Incorrecto')
        else:
            print ('Password y/o usuario Incorrecto')
            
    def ShowMenu(self):
    
        """Metodo que muestra el menu de Bienvenida y opciones iniciales (Login
        y crear usuario). Devuelve False si se eligio Login para dar 
        paso a ShowUserMenu y True si se eligio cualquier otra opcion, para forzar
        otro ciclo de main"""
    
        print('Bienvenido a la app de compra y venta de moneda')
        print('Ingrese la Opcion que desea Realizar:')
        print('1-Login','2-Crear Usuario',sep='\n')
        try:
            opt=int(input())
            if opt==1:
                self.ShowLogin()
                self.ShowAccounts()
                return False
            elif opt==2:
                myOpIfce=OpInterface(self.admin)
                myOpIfce.BuildUser() 
                return True
            else:
                print('Opcion Incorrecta')
                return True
        except:
            print('Opcion Incorrecta')
            return True

    def ShowUserMenu(self):
    
        """Metodo que muestra el menu de Usuario y opciones especificas
        (Comprar,depositar, crear cuenta).Devuelve True si realizo una 
        operacion con exito y False si se ingreso la opcion Salir"""

        myOpIfce=OpInterface(self.admin)
        print('Ingrese la Opcion que desea Realizar, cualquier otra para salir')
        print('1-Comprar','2-Depositar','3-Crear Cuenta',sep='\n')
        try:
            opt=int(input())
            if opt==1:
                myOpIfce.Buy() 
                self.ShowAccounts()
                return True
            elif opt==2:
                myOpIfce.Deposit() 
                self.ShowAccounts()
                return True   
            elif opt==3:
                myOpIfce.BuildAccount() 
                self.ShowAccounts()
                return True
            else:
                print('Adios')
                return False
        except:
            print('Adios')
            return False
            
    def ShowAccounts(self):
    
        """Metodo que muestra las cuentas y saldos del usuario loggeado"""
        
        result = self.admin.CheckAccount()
        if result is None:
            pass#usuario incorrecto
        elif result == False:
            print ('No hay cuentas')
        else:
            print ('Cuentas:')
            for count in result:
                print('Moneda-> '+count['currency']+\
                ' Saldo-> {:.2f}'.format(count['amount']))
                
class OpInterface(object):

    """Clase que opera como interfaz de Usuario para las 
operaciones compra, deposito, creacion de usuarios y cuentas
Para usar sus metodos el usuario debe estar correctamente loggeado
excepto por BuildUser"""
    
    def __init__(self,admin):
        self.admin=admin
        
    def Buy(self):
    
        """Metodo que funciona como interfaz de usuario para la compra o
        intrecambio de moneda. Toma los datos moneda origen, destino, 
        cantidad a comprar o a debitar e informa sobre el resultado de la
        operacion"""
        
        org=input('Moneda Origen:').upper()
        dst=input('Moneda Destino:').upper()
        op=input("1-Cantidad a comprar\n2-Cantidad a debitar:\n")
        if op=='1':
            op='BUY'
        elif op=='2':
            op='DEBIT'
        else:
            print('Opcion Incorrecta')
            return
        cnt=Decimal(input('Cantidad:'))
        MyBuyer=Buyer(operation=op,org=org,dst=dst,cnt=cnt)
        res=MyBuyer.prepare(self.admin)
        if res != False:
        
            if res['status']=='OK':
            
                print('Saldo Suficiente, Su balance sera {:.2f} {} y {:.2f} {}'
                    .format(res['bal_org'],org,res['bal_dst'],dst))
                    
                ack=input('Desea Comfirmar?(S/N):\n')
                if ack.lower()=='s':
                    if (MyBuyer.validate(self.admin,
                        res['bal_org'],res['bal_dst'])) == True:
                        
                        print('Compra Exitosa!')
                        
                    else:
                        print('Error')
                else:
                    print('Cancelado')
                    
            elif res['status']=='NOT OK': 
            
                print('Saldo Insuficiente, Su balance sera {:.2f} {} y {:.2f} {}'
                    .format(res['bal_org'],org,res['bal_dst'],dst))
                    
                return
                
            else:
                return
        else:
            print('No existe la cuenta origen y/o destino, creela primero')
            return
           
    def Deposit(self):
            
        """Metodo que funciona como interfaz de usuario para el deposito de ARS.
        Toma los datos de cantidad de ARS y llama al metodo de cobro e informa 
        el resultado de la operacion"""
        
        cnt=Decimal(input('Ingrese la Cantidad de ARS a depositar:\n'))
        MyDepositor=Depositor(cnt)
        MyCollector=Collector()
        res=MyDepositor.prepare(self.admin)
        
        print('Luego del deposito su Saldo sera: {:.2f} ARS'.format(res))
        ack=input('Desea Comfirmar?(S/N):\n')
        
        if ack.lower()=='s':
            rv=MyDepositor.validate(self.admin)
            rv2=MyCollector.validate() #aqui realizaria el cobro
            if (rv and rv2) == True:
                print('Deposito Exitoso!')
            else:
                print('Error')
        else:
            print('Cancelado')

    def BuildAccount(self):
    
        """Metodo que funciona como interfaz de usuario para la creacion de cuenta.
        Toma los datos de la moneda de cuenta e informa el resultado de la operacion"""

        crncy=input('Ingrese la Moneda de la Cuenta a Crear:\n')
        MyAccountBuilder=AccountBuilder(crncy)
        res=MyAccountBuilder.prepare(self.admin)
        if res==False:
            print('La cuenta ya existe')
            return
        elif res is None:
            print('La Moneda no existe')
            return
        else:
            ack=input(
            'Desea Crear una nueva Cuenta en {}?(S/N):\n'.format(crncy.upper()))
            if ack.lower()=='s':
                rv=MyAccountBuilder.Build(self.admin)
                if rv == True:
                    print('Cuenta Creada con Exito!')
                else:
                    print('Error')
            else:
                print('Cancelado')
            
    def BuildUser(self):
    
        """Metodo que funciona como interfaz de usuario para la creacion de Usuario.
        Toma los datos usuario y password e informa el resultado de la operacion"""

        name=input('Ingrese el nombre Usuario a Crear:\n')
        pwd=input('Ingrese la clave de Acceso:\n')
        MyUserBuilder=UserBuilder(name,pwd)
        rv=MyUserBuilder.validateUser(self.admin)
        if rv==False:
            print('El ususario ya Existe')
            return
        else:
            pwd=input('Ingrese Nuevamente la clave de Acceso:\n')
            rv=MyUserBuilder.validatePwd(pwd)
            if rv== False:
                print('Las claves no coinciden')
                return
            else:
                ack=input('Comfirma la creacion de Usuario?(S/N):\n')
                if ack.lower()=='s':
                    rv=MyUserBuilder.Build(self.admin)
                    if rv==False:
                        print('Error')
                        return
                    else:
                        print('Usuario Creado con exito')
                        return
                else:
                    print('Cancelado')
                    return
    
             