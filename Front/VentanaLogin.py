from PyQt5.QtWidgets import QMainWindow, QApplication
from Front.login import Ui_primera
from Front.administrador.VentanasAdmin import VentanasAdmin
from BD.Conexion import *
from Front.administrador.VentanasAdmin2 import VentanasAdmin2, EmerRetorno2

from Front.trabajador.VentanasTrabajador import VentanasTrabajador
from Front.trabajador.VentanaAdminBase import VentanaAdminBase
from Front.emerComunes.retorno import Ui_Dialog


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class EmerRetorno():

    def __init__(self):
        self.emerRetorno = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.emerRetorno)

        self.ui.botAceRet.clicked.connect(self.cerrar_ventana)

    def imprimir_retorno(self, retorno_emer):
        self.ui.LRetorno.setText(retorno_emer)

    def cerrar_ventana(self):
        self.emerRetorno.close()



def validacion(id_usuario, contrasena):
    print('llegue', id_usuario, contrasena)
    if id_usuario.isdigit() and contrasena.isdigit():
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE id_usuario = " + str(id_usuario))
                usuario = cursor.fetchone()
                print(usuario)
                if usuario:
                    usuario_contrasena = usuario[1]
                    if usuario_contrasena == int(contrasena):
                        print(usuario_contrasena)
                        return usuario
                    else:
                        return 'La contraseña la tienes incorrecta'
                else:
                    return 'No existe el usuario'
        except psycopg2.Error as e:
            return ("Ocurrio un error al consultar")
    else:
        return ('El id y la contraseña tienen que ser números')

class Login():

    def __init__(self):
        self.login = QMainWindow ()
        super().__init__()
        self.ui = Ui_primera ()
        self.ui.setupUi(self.login)

        self.ui.botCanLog.clicked.connect(self.cancelar_logear)
        self.ui.botAceLog.clicked.connect(self.aceptar_logear)


    def cancelar_logear(self):

        self.ui.LIdUsu.clear()
        self.ui.LConUsu.clear()

    def crear_ventana_retorno(self, retorno):
        print('llegue a crear ventana')
        self.ventana_emergente = EmerRetorno()
        self.ventana_emergente.emerRetorno.show()
        self.ventana_emergente.imprimir_retorno(str(retorno))

    def aceptar_logear(self):
        ret_val = validacion(self.ui.LIdUsu.text(), self.ui.LConUsu.text())
        print(ret_val)
        if isinstance(ret_val, str):
            self.crear_ventana_retorno(str(ret_val))
        else:
            if ret_val[4] == 'Trabajador':
                print(ret_val)
                self.login.close()
                admin = VentanasTrabajador ()
                admin.recibir_datos(ret_val)
                admin.show()
            elif ret_val[4] == 'Administrador':
                print(ret_val)
                self.login.close()
                admin = VentanasAdmin()
                admin.recibir_datos(ret_val)
                admin.show()
            elif ret_val[4] == 'Administrador2':
                print(ret_val)
                self.login.close()
                admin = VentanasAdmin2()
                admin.recibir_datos(ret_val)
                admin.show()

            elif ret_val[4] == 'Administrador Base':
                print(ret_val)
                self.login.close()
                admin = VentanaAdminBase()
                admin.recibir_datos(ret_val)
                admin.show()

            elif ret_val[4] == 'Visualizador':
                print(ret_val)
                self.login.close()
                admin = VentanasTrabajador()
                admin.recibir_datos(ret_val)
                admin.show()
            else:
                print('puse algo malo')

