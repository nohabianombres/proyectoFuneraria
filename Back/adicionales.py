from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Front.generar_pdfs import pdf_factura_caja

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()


class Adicionales ():

    def crear_factura_caja (self, ciudad, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, cantidades, valores_unitarios, usuario_encargado):

        print('entre a crear factura de caja')
        fecha_actual = datetime.now().date()
        cantidades_int = [int(x) for x in cantidades]
        valores_unitarios_int = [int(y) for y in valores_unitarios]

        valor_total = sum(x * y for x, y in zip(cantidades_int, valores_unitarios_int))

        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO adicionales(ciudad, fecha, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, cantidades, valores_unitarios, valor_total, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (ciudad, fecha_actual, nombre_comprador, int(documento_comprador), nombre_vendedor, descripciones, cantidades_int, valores_unitarios_int, valor_total, valor_total))
            conexion.commit()
            print('Fac creada')
            pdf_factura_caja(ciudad, fecha_actual, usuario_encargado,nombre_comprador, descripciones,valor_total,0)
            return ("Factura de caja creada")
        except psycopg2.Error as e:
            return ("Ocurrió un error al crear la factura de caja:" + str(e))

    def eliminar_factura_caja (self, id_adicionales):
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM adicionales WHERE id_adicional=" + str(id_adicionales)
                cursor.execute(consulta)
            conexion.commit()
            return ("Factura eliminada correctamente")
        except psycopg2.Error as e:
            return ("Error al eliminar la factura" + str(e))

    def consultar_saldo_facturas_documento (self, documento):
        self.saldo = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_adicional,saldo, nombre_comprador, documento_comprador, saldo, fecha FROM adicionales WHERE documento_comprador=%s AND saldo <> 0" , (str(documento),))
                datos_factura = cursor.fetchall()
                if datos_factura:
                    for saldo_id in datos_factura:
                        self.saldo.append(saldo_id[1])
                    print('Sus valores a pagar son los siguientes:', datos_factura)
                    print('Su valor total a pagar es el siguiente:' ,sum(self.saldo))
                    return datos_factura, sum(self.saldo)
                else:
                    print('No existe ninguna factura')
                    return 'No se encontro ninguna factura'
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: " + str(e)

    def abonar_factura_caja (self, id_adicional, valor_abonado, usuario_encargado):
        fecha_actual = datetime.now().date()
        print('llegue a la funcion')
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM adicionales WHERE id_adicional=" + str(id_adicional))
                factura_caja = cursor.fetchone()
                print(factura_caja)
                valor_saldo = factura_caja [-1]
                print(valor_saldo)
                if int(valor_saldo) >= int(valor_abonado):
                    print('entre al if')
                    try:
                        with conexion.cursor() as cursor:
                            consulta = "UPDATE adicionales SET saldo = saldo - %s WHERE id_adicional = %s"
                            cursor.execute(consulta, (valor_abonado, id_adicional))
                            conexion.commit()
                        print('Los valores se han actualizado correctamente.')
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "INSERT INTO facturas_adicionales(documento_comprador, nombre_comprador, fecha, nombre_vendedor, id_factura, valor_abonado, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                                cursor.execute(consulta, (int(factura_caja[4]), factura_caja[3], fecha_actual, usuario_encargado, int(factura_caja[0]), int(valor_abonado), False))
                            conexion.commit()
                            print("Factura de caja creada")

                            try:
                                with conexion.cursor() as cursor:
                                    cursor.execute(
                                        """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                    ultimo_dato_insertado = cursor.fetchone()
                                    print(ultimo_dato_insertado)
                                try:
                                    with conexion.cursor() as cursor:
                                        consulta = "INSERT INTO saldo(valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                        cursor.execute(consulta, (
                                        int(valor_abonado), fecha_actual, ultimo_dato_insertado[6],
                                        ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                        ultimo_dato_insertado[9] + (int(valor_abonado) / 2),
                                        ultimo_dato_insertado[10] + (int(valor_abonado) / 2),
                                        ultimo_dato_insertado[11] + int(valor_abonado), False))
                                    conexion.commit()
                                    print("Saldo cambiado")
                                    pdf_factura_caja(factura_caja[1], fecha_actual, usuario_encargado, factura_caja[3],
                                                     factura_caja[6], valor_saldo-valor_abonado, valor_abonado)
                                    return 'El abono y lo demás a sido generado con exito'
                                except psycopg2.Error as e:
                                    return ("Ocurrió un error al crear el ultimo saldo:")
                            except psycopg2.Error as e:
                                return ("Ocurrió un error al seleccionar el ultimo:", e)





                        except psycopg2.Error as e:
                            print("Ocurrió un error al crear la el recibo del abono:" , e)
                    except psycopg2.Error as e:
                        return "Ocurrió un error al abonar: " + str(e)
                else:
                    return ('La deuda no es de tanto dinero')
        except psycopg2.Error as e:
            return "Ocurrio un error al consultar: " + str(e)







