from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()
class Gastos ():

    def gasto_jefe1 (self, gasto, valor, nombre_usuario):
        if valor.isdigit() :
            fecha_actual = datetime.now().date()
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO gastos(gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (gasto, valor, nombre_usuario,fecha_actual , True, False, False, False, False))
                conexion.commit()
                print("Gasto asentado")
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute("""SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                        ultimo_dato_insertado = cursor.fetchone()
                        print(ultimo_dato_insertado)

                    try:
                        saldo_jefe1 = (ultimo_dato_insertado[9] - int(ultimo_dato_insertado[-7]) - int(valor))
                        print('este es el saldo 1',saldo_jefe1)
                        saldo_jefe2 = (ultimo_dato_insertado[10] - int(ultimo_dato_insertado[-6]))
                        print(saldo_jefe2)
                        print(ultimo_dato_insertado[-7])
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO saldo(gasto, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            cursor.execute(consulta, (gasto, int(valor), fecha_actual,int(ultimo_dato_insertado[-7]) + int(valor),int(ultimo_dato_insertado[-6]), int(ultimo_dato_insertado[-5]),saldo_jefe1, saldo_jefe2,int(ultimo_dato_insertado[-2]) - int(valor), False))
                            conexion.commit()
                        print("Saldo cambiado")
                        return 'El gasto y lo demás a sido generado con exito'
                    except psycopg2.Error as e:
                        return ("Ocurrió un error al crear el último saldo:", e)
                except psycopg2.Error as e:
                    return ("Ocurrió un error al seleccionar el último:", e)

            except psycopg2.Error as e:
                return ( "Ocurrió un error al asentar el gasto:")
        else:
            return "No es un valor correcto"

    def gasto_jefe2(self, gasto, valor, nombre_usuario):
        if valor.isdigit():
            fecha_actual = datetime.now().date()
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO gastos(gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (gasto, int(valor), nombre_usuario, fecha_actual, False, True, False, False, False))
                conexion.commit()
                print("Gasto asentado")
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute(
                            """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                        ultimo_dato_insertado = cursor.fetchone()
                        print(ultimo_dato_insertado)
                    try:
                        saldo_jefe1 = (ultimo_dato_insertado[9] - int(ultimo_dato_insertado[-7]))
                        print('este es ', saldo_jefe1)
                        saldo_jefe2 = (ultimo_dato_insertado[10] - int(ultimo_dato_insertado[-6]) - int(valor))


                        print(saldo_jefe2)
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO saldo(gasto, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            cursor.execute(consulta, (gasto, valor, fecha_actual,ultimo_dato_insertado[-7], int(ultimo_dato_insertado[-6]) + int(valor), ultimo_dato_insertado[-5],saldo_jefe1, saldo_jefe2, int(ultimo_dato_insertado[-2]) - int(valor), False))
                        conexion.commit()
                        print("Saldo cambiado")
                        return 'El gasto y lo demás a sido generado con exito'
                    except psycopg2.Error as e:
                        return ("Ocurrió un error al crear el ultimo saldo:", e)
                except psycopg2.Error as e:
                    return ("Ocurrió un error al seleccionar el ultimo:", e)
            except psycopg2.Error as e:
                return ("Ocurrió un error al asentar el gasto:", e)
        else:
            return "No es un valor correcto"

    def gasto_funeraria (self, gasto, valor, nombre_usuario):
        if valor.isdigit():
            print('entre a gasto funeraria')
            fecha_actual = datetime.now().date()
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO gastos(gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (gasto, int(valor), nombre_usuario, fecha_actual, False, False, True, False, False))
                    conexion.commit()
                print("Gasto asentado")
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute(
                            """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                        ultimo_dato_insertado = cursor.fetchone()
                        print(ultimo_dato_insertado)
                    try:
                        saldo_jefe1 = ultimo_dato_insertado[9] - (int(valor)/2)

                        saldo_jefe2 = ultimo_dato_insertado[10] - (int(valor)/2)

                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO saldo(gasto, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            cursor.execute(consulta, (gasto, int(valor), fecha_actual,ultimo_dato_insertado[-7] , ultimo_dato_insertado[-6] ,int(valor)+ int(ultimo_dato_insertado[-5]),saldo_jefe1 , saldo_jefe2 ,int(ultimo_dato_insertado[-2]) - int(valor), False))
                            conexion.commit()
                        print("Saldo cambiado")
                        return 'El gasto y lo demás a sido generado con exito'
                    except psycopg2.Error as e:
                        return ("Ocurrió un error al crear el ultimo saldo:")
                except psycopg2.Error as e:
                    return ("Ocurrió un error al seleccionar el ultimo:", e)
            except psycopg2.Error as e:
                return ("Ocurrió un error al asentar el gasto:")
        else:
            return "No es un valor correcto"
    def gastos_sin_revisar(self):
        print('llegue a la funcion gastos_sin_revisar')
        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT id_gasto, gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado FROM gastos WHERE revisado = False;")
                gastos_sin_revisar = cursor.fetchall()
                for gasto_sin_revisar in gastos_sin_revisar:
                    print(gasto_sin_revisar)
                return gastos_sin_revisar
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar:"


    def revisar_gastos (self, id_gasto):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE gastos SET revisado = %s WHERE id_gasto = %s"
                cursor.execute(consulta, (True, id_gasto))
                conexion.commit()
                print('revise el gasto')
        except psycopg2.Error as e:
            return ("Ocurrió un error al pagar: ", e)


