
from BD.Conexion import *
from datetime import datetime, timedelta
from Front.crearExcel import crear_excel_gastos, crear_excel_saldo, crear_excel_colillas, crear_excel_adicionales
basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()


class Liquidacion ():

    def generar_liquidacion(self, id_jef1, id_jef2, con_jef1, con_jef2):
        if id_jef1.isdigit() and id_jef2.isdigit() and con_jef1.isdigit() and con_jef2.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM usuario WHERE cargo=%s",
                        ("Administrador",))
                    datos_jefe1 = cursor.fetchone()
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)

            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM usuario WHERE cargo=%s",
                        ("Administrador2",))
                    datos_jefe2 = cursor.fetchone()
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)

            if datos_jefe1[1] == int(con_jef1) and datos_jefe1[0] == int(id_jef1) and datos_jefe2[0] == int(id_jef2) and datos_jefe2[1] == int(con_jef2):
                fecha_actual = datetime.now().date()

                try:
                    with conexion.cursor() as cursor:
                        # Consulta para extraer los datos de gastos antes de marcarlos como liquidados
                        consulta_select = """
                                        SELECT id_gasto, gasto, valor, nombre_usuario, fecha
                                        FROM gastos
                                        WHERE liquidado = %s
                                    """
                        cursor.execute(consulta_select, (False,))
                        datos_gastos = cursor.fetchall()
                        crear_excel_gastos(datos_gastos)
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE gastos SET liquidado = %s WHERE liquidado = %s"
                                cursor.execute(consulta, (True, False))
                                conexion.commit()
                            print("Los gastos se han marcado como liquidados.")



                            try:
                                with conexion.cursor() as cursor:
                                    # Consulta para extraer los datos de gastos antes de marcarlos como liquidados
                                    consulta_select = """
                                                    SELECT id_factura,nombre_comprador,documento_comprador, nombre_vendedor, valor_abonado,fecha
                                                    FROM facturas_adicionales
                                                    WHERE liquidado = %s
                                                """
                                    cursor.execute(consulta_select, (False,))
                                    datos_adicionales = cursor.fetchall()
                                    crear_excel_adicionales(datos_adicionales)






                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "UPDATE facturas_adicionales SET liquidado = %s WHERE liquidado = %s"
                                            cursor.execute(consulta, (True, False))
                                            conexion.commit()
                                        print("Los abonosa  facturas de caja se han marcado como liquidados.")

                                        try:
                                            with conexion.cursor() as cursor:
                                                # Consulta para extraer los datos de gastos antes de marcarlos como liquidados
                                                consulta_select = """
                                                                SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario,fecha_pago
                                                                FROM colillas
                                                                WHERE liquidado = %s
                                                            """
                                                cursor.execute(consulta_select, (False,))
                                                datos_colillas = cursor.fetchall()
                                                crear_excel_colillas(datos_colillas)




                                                try:
                                                    with conexion.cursor() as cursor:
                                                        consulta = "UPDATE colillas SET liquidado = %s WHERE liquidado = %s"
                                                        cursor.execute(consulta, (True, False))
                                                        conexion.commit()
                                                    print("Las colillas se han marcado como liquidados.")

                                                    try:
                                                        with conexion.cursor() as cursor:
                                                            # Consulta para extraer los datos de saldo antes de marcarlos como liquidados
                                                            consulta_select = """
                                                                                        SELECT socio, gasto, descripciones, fecha, valor, funeraria, jefe1, jefe2
                                                                                        FROM saldo
                                                                                        WHERE liquidado = %s
                                                                                    """
                                                            cursor.execute(consulta_select, (False,))
                                                            datos_saldo = cursor.fetchall()
                                                            crear_excel_saldo(datos_saldo)


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
                                                        print("Ocurrió un error al marcar los gastos como liquidados:", e)
                                                except psycopg2.Error as e:
                                                    print("Ocurrió un error al marcar las colillas como liquidados:", e)

                                        except psycopg2.Error as e:
                                            print("Ocurrió un error al consultar las colillas por liquidar :", e)
                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al marcar las facturas de caja como liquidados:", e)
                            except psycopg2.Error as e:
                                print("Ocurrió un error al consultar los adicionales por liquidar :", e)
                        except psycopg2.Error as e:
                            print("Ocurrió un error al marcar los gastos como liquidados:", e)

                except psycopg2.Error as e:
                    print("Ocurrió un error al consultar los gastos por liquidar :", e)

            else:
                return ('Los datos de los administradores estan erroneos')
        else:
            return "Los usuarios y contraseñas deben ser números"