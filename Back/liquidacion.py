
from BD.Conexion import *
from datetime import datetime, timedelta


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()


class Liquidacion ():

    def generar_liquidacion(self, id_jef1, con_jef1, id_jef2, con_jef2):
        '''try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM usuario WHERE id_usuario = %s""", int(id_jef1))
                datos_jefe1 = cursor.fetchone()
                print(datos_jefe1)
        except psycopg2.Error as e:
            print ("Ocurrió un error al seleccionar el jefe 1 :" + str(e))

        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM usuario WHERE id_usuario = %s""", int(id_jef2))
                datos_jefe1 = cursor.fetchone()
                print(datos_jefe1)
        except psycopg2.Error as e:
            print ("Ocurrió un error al seleccionar el jefe 2:" + str(e))
    '''



        fecha_actual = datetime.now().date()
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE gastos SET liquidado = %s WHERE liquidado = %s"
                cursor.execute(consulta, (True, False))
                conexion.commit()
            print("Los gastos se han marcado como liquidados.")
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE facturas_adicionales SET liquidado = %s WHERE liquidado = %s"
                    cursor.execute(consulta, (True, False))
                    conexion.commit()
                print("Los abonosa  facturas de caja se han marcado como liquidados.")
                try:
                    with conexion.cursor() as cursor:
                        consulta = "UPDATE colillas SET liquidado = %s WHERE liquidado = %s"
                        cursor.execute(consulta, (True, False))
                        conexion.commit()
                    print("Las colillas se han marcado como liquidados.")
                    try:
                        with conexion.cursor() as cursor:
                            consulta = "UPDATE saldo SET liquidado = %s WHERE liquidado = %s"
                            cursor.execute(consulta, (True, False))
                            conexion.commit()
                        print("Los saldos se han marcado como liquidados.")
                        try:
                            with conexion.cursor() as cursor:
                                cursor.execute(
                                    """SELECT gastos_jefe1, gastos_jefe2, jefe1, jefe2 FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                ultimo_dato_insertado = cursor.fetchone()
                                print(ultimo_dato_insertado)
                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO saldo(valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (0, fecha_actual, 0, 0, 0, 0, 0, 0, False))
                                    conexion.commit()
                                print("Saldo cambiado")
                                return ultimo_dato_insertado
                            except psycopg2.Error as e:
                                print("Ocurrió un error al crear el ultimo saldo:",e)
                        except psycopg2.Error as e:
                            print("Ocurrió un error al seleccionar el ultimo:", e)
                    except psycopg2.Error as e:
                        print("Ocurrió un error al marcar los saldos como liquidados:", e)
                except psycopg2.Error as e:
                    print("Ocurrió un error al marcar las colillas como liquidados:", e)
            except psycopg2.Error as e:
                print("Ocurrió un error al marcar las facturas de caja como liquidados:", e)
        except psycopg2.Error as e:
            print("Ocurrió un error al marcar los gastos como liquidados:", e)