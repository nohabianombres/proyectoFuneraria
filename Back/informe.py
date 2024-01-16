from BD.Conexion import *
from datetime import datetime, timedelta


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Informes ():

    def mostrar_ultimo_saldo(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""SELECT id_saldo, socio, gasto, descripciones, valor, funeraria, fecha FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                ultimo_dato_insertado = cursor.fetchone()
                return (ultimo_dato_insertado)
        except psycopg2.Error as e:
            print("Ocurrió un error al seleccionar el ultimo:", e)

    def mostrar_gastos_no_liquidados(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id_gasto, gasto, valor, nombre_usuario, fecha FROM gastos WHERE liquidado = %s"
                cursor.execute(consulta, (False,))
                gastos = cursor.fetchall()
            print(gastos)
            return gastos
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: " + str(e)

    def mostrar_colillas_no_liquidadas(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT socio, valor_mes,desde_fecha, hasta_fecha, usuario, fecha_pago  FROM colillas WHERE liquidado = %s"
                cursor.execute(consulta, (False,))
                gastos = cursor.fetchall()
            print(gastos)
            return gastos
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: " + str(e)

    def mostrar_saldo_no_liquidado (self):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id_saldo, socio, gasto, descripciones, valor, funeraria, fecha FROM saldo WHERE liquidado = %s"
                cursor.execute(consulta, (False,))
                gastos = cursor.fetchall()
            print(gastos)
            return gastos
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: " + str(e)

    def mostrar_adicionales_no_liquidado(self):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT id_abono, id_factura,nombre_comprador, nombre_vendedor, valor_abonado,fecha FROM facturas_adicionales WHERE liquidado = %s"
                cursor.execute(consulta, (False,))
                gastos = cursor.fetchall()
            print(gastos)
            return gastos
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: " + str(e)