from BD.Conexion import *

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()


class Usuarios ():

    def crear_usuario (self,contrasena, nombre, documento, cargo):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuario(contrasena, nombre, documento, cargo) VALUES (%s, %s, %s, %s);"
                cursor.execute(consulta, (contrasena, nombre, documento, cargo))
            conexion.commit()
            return ("Usuario creado")
        except psycopg2.Error as e:
            return ( "Ocurrió un error al crear el usuario :", e)

    def eliminar_usuario(self, id_usuario):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM usuario WHERE id_usuario=" + str(id_usuario)
                cursor.execute(consulta)

            # Comprobar si se eliminó algún registro
            if cursor.rowcount > 0:
                conexion.commit()
                print("Se eliminó correctamente")
                return ("Se eliminó correctamente")
            else:
                print("No se pudo eliminar el usuario. ID de usuario no encontrado.")
                return ("No se pudo eliminar el usuario. ID de usuario no encontrado.")

        except psycopg2.Error as e:
            return ("Error al eliminar el usuario:", str(e))

    def mostrar_usuarios (self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombre, documento, cargo FROM usuario;")
                usuarios = cursor.fetchall()
                return (usuarios)
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: ", str(e)
