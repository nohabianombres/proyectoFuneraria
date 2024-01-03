from PyQt5.QtWidgets import QMainWindow, QApplication
from Front.login import Ui_primera
from Front.administrador.VentanasAdmin import VentanasAdmin
from BD.Conexion import *
from Front.administrador.VentanasAdmin2 import VentanasAdmin2, EmerRetorno2

from Front.trabajador.VentanasTrabajador import VentanasTrabajador


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion = basedatos.conectar()

def validacion(id_usuario, contrasena):
    print('llegue', id_usuario, contrasena)
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

class Login():

    def __init__(self):
        self.login = QMainWindow ()
        super().__init__()
        self.ui = Ui_primera ()
        self.ui.setupUi(self.login)

        self.ui.botCanLog.clicked.connect(self.cancelar_logear)
        self.ui.botAceLog.clicked.connect(self.aceptar_logear)

    def cancelar_logear(self, stacked_widget):

        pass

    def aceptar_logear(self):
        ret_val = validacion(self.ui.LIdUsu.text(), self.ui.LConUsu.text())
        print(ret_val)
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
        elif ret_val[4] == 'Visualizador':
            print(ret_val)
            self.login.close()
            admin = VentanasTrabajador()
            admin.recibir_datos(ret_val)
            admin.show()
        else:
            print('puse algo malo')

