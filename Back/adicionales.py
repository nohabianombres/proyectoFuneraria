from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Front.generar_pdfs import pdf_factura_caja

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Adicionales ():

    def crear_factura_caja(self, nombre_comprador, documento_comprador, descripciones, valores_unitarios, usuario_encargado, valor_abonar, nota, telefono):
        if documento_comprador.isdigit() and valor_abonar.isdigit():
            print('Entre a crear factura de caja')
            fecha_actual = datetime.now().date()
            if int(valor_abonar) > 0:

                # Verificar si todos los elementos en las listas son dígitos
                if all(y.isdigit() for y in valores_unitarios):
                    valores_unitarios_int = [int(y) for y in valores_unitarios]
                    valor_total = int(sum(valores_unitarios_int))
                
                    if valor_total >= int(valor_abonar):
                        try:
                            with conexion.cursor() as cursor:
                                # Inserta datos en la tabla 'adicionales' y obtiene el id_factura generado
                                consulta = """
                                    INSERT INTO adicionales(fecha, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, valores_unitarios, valor_total, saldo, nota_factura, telefono) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    RETURNING id_adicional;
                                """
                                cursor.execute(consulta, (
                                    fecha_actual, nombre_comprador, int(documento_comprador), usuario_encargado,
                                    descripciones, valores_unitarios_int, valor_total,
                                    valor_total - int(valor_abonar), nota, telefono
                                ))

                                # Obtener el id_factura generado automáticamente
                                id_factura = cursor.fetchone()[0]
                                print(id_factura)

                            conexion.commit()
                            print('Factura creada')

                            try:
                                with conexion.cursor() as cursor:
                                    # Inserta datos en la tabla 'facturas_adicionales' usando el id_factura obtenido
                                    consulta = """
                                        INSERT INTO facturas_adicionales(documento_comprador, nombre_comprador, fecha, nombre_vendedor, id_factura, valor_abonado, liquidado) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                                    """
                                    cursor.execute(consulta, (
                                        int(documento_comprador), nombre_comprador, fecha_actual, usuario_encargado,
                                        id_factura, valor_abonar, False
                                    ))

                                conexion.commit()
                                print("Factura de caja creada")

                                try:
                                    with conexion.cursor() as cursor:
                                        cursor.execute(
                                            """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)"""
                                        )
                                        ultimo_dato_insertado = cursor.fetchone()
                                        print(ultimo_dato_insertado)

                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = """
                                                INSERT INTO saldo(valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, descripciones, gasto, socio) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                                            """
                                            cursor.execute(consulta, (
                                                int(valor_abonar), fecha_actual, ultimo_dato_insertado[6],
                                                ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                                ultimo_dato_insertado[9] + (int(valor_abonar) / 2),
                                                ultimo_dato_insertado[10] + (int(valor_abonar) / 2),
                                                ultimo_dato_insertado[11] + int(valor_abonar), False, descripciones, '',
                                                0
                                            ))
                                        conexion.commit()
                                        print("Saldo cambiado")
                                        pdf_factura_caja("Sonson", fecha_actual, usuario_encargado, nombre_comprador,
                                                         documento_comprador, descripciones,valores_unitarios_int,
                                                         valor_total - int(valor_abonar),
                                                         int(valor_abonar), valor_total)
                                        return "Factura de caja creada"
                                    except psycopg2.Error as e:
                                        return "Ocurrió un error al crear el último saldo: " + str(e)
                                except psycopg2.Error as e:
                                    return "Ocurrió un error al seleccionar el último saldo: " + str(e)
                            except psycopg2.Error as e:
                                return "Ocurrió un error al crear la factura de caja: " + str(e)
                        except psycopg2.Error as e:
                            return "Ocurrió un error al crear la factura de caja: " + str(e)
                    else:
                        return "El valor abonar es mayor al valor total de la factura"
                else:
                    return "La cantidad y valor unitario deben ser únicamente de números"
            else:
                if all(y.isdigit() for y in valores_unitarios):
                    fecha_actual = datetime.now().date()
                    valores_unitarios_int = [int(y) for y in valores_unitarios]

                    valor_total = int(sum(valores_unitarios_int))

                    try:
                        with conexion.cursor() as cursor:
                            consulta = """
                                INSERT INTO adicionales(fecha, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, valores_unitarios, valor_total, saldo, nota_factura) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                            """
                            cursor.execute(consulta, (
                                fecha_actual, nombre_comprador, int(documento_comprador), usuario_encargado,
                                descripciones, valores_unitarios_int, valor_total, valor_total, nota
                            ))
                        conexion.commit()
                        print('Factura creada')
                        pdf_factura_caja("Sonson", fecha_actual, usuario_encargado, nombre_comprador,
                                         documento_comprador, descripciones, valor_total, 0, valor_total)
                        return "Factura de caja creada"
                    except psycopg2.Error as e:
                        return "Ocurrió un error al crear la factura de caja: " + str(e)
                else:
                    return "La cantidad y valor unitario deben ser únicamente de números"
        else:
            return "El documento del comprador y el valor abonar deben ser números"

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
        if documento.isdigit() :
            self.saldo = []
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT id_adicional,saldo, nombre_comprador, documento_comprador, saldo, fecha, nota_factura, telefono FROM adicionales WHERE documento_comprador=%s AND saldo > 0" , (str(documento),))
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
        else:
            return "No es un número de documento correcto"

    def consultar_abonos_facturas_documento (self, documento):
        if documento.isdigit() :
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT id_factura, nombre_comprador, documento_comprador, fecha, valor_abonado, nombre_vendedor FROM facturas_adicionales WHERE documento_comprador=%s" , (str(documento),))
                    datos_facturas = cursor.fetchall()
                    if datos_facturas:
                        print(datos_facturas)
                        return datos_facturas
                    else:
                        print('No existe ninguna factura')
                        return 'No se encontro ninguna factura'
            except psycopg2.Error as e:
                return "Ocurrio un error al consultar: " + str(e)
        else:
            return "No es un número de documento correcto"

    def abonar_factura_caja (self, id_adicional, valor_abonado, usuario_encargado):
        if id_adicional.isdigit() and valor_abonado.isdigit():
            fecha_actual = datetime.now().date()
            print('llegue a la funcion')
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM adicionales WHERE id_adicional=" + str(id_adicional))
                    factura_caja = cursor.fetchone()
                    print(factura_caja)
                    valor_saldo = factura_caja [-2]
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
                                            consulta = "INSERT INTO saldo(valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, descripciones, gasto, socio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (
                                            int(valor_abonado), fecha_actual, ultimo_dato_insertado[6],
                                            ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                            ultimo_dato_insertado[9] + (int(valor_abonado) / 2),
                                            ultimo_dato_insertado[10] + (int(valor_abonado) / 2),
                                            ultimo_dato_insertado[11] + int(valor_abonado), False, factura_caja[6], '',0))
                                        conexion.commit()
                                        print("Saldo cambiado")
                                        pdf_factura_caja(factura_caja[1], fecha_actual, usuario_encargado, factura_caja[3],factura_caja[4],
                                                         factura_caja[6], valor_saldo-int(valor_abonado), valor_abonado,factura_caja[9])
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
        else:
            return "El id de la factura y el valor abonar deben ser números"


    def mostrar_cartera(self):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id_adicional, fecha, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, valor_total, saldo 
                    FROM adicionales 
                    WHERE saldo > 0 
                    ORDER BY id_adicional ASC;
                """
                cursor.execute(consulta)
                cartera = cursor.fetchall()
            print(cartera)
            return cartera
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: " + str(e)





