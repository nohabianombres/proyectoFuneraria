from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Front.generar_pdfs import pdf_colilla
import psycopg2.extras
from itertools import zip_longest
from array import array

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Polizas ():

    def crear_poliza (self, socio, nombres, documentos, fechas_nacimiento, parentesco_titular, valor_mes, numero_meses, usuario_encargado):
        valor_por_defecto = ''
        print(nombres)

        # Encuentra la longitud máxima entre las listas
        max_length = max(len(nombres), len(documentos), len(fechas_nacimiento), len(parentesco_titular))

        print(parentesco_titular)
        print(nombres)

        # Rellena o recorta las listas para que tengan la misma longitud
        nombres = list(nombres) + [valor_por_defecto] * (max_length - len(nombres))
        print(nombres)
        documentos = list(documentos) + [valor_por_defecto] * (max_length - len(documentos))
        fechas_nacimiento = list(fechas_nacimiento) + [valor_por_defecto] * (max_length - len(fechas_nacimiento))
        parentesco_titular = list(parentesco_titular) + [valor_por_defecto] * (max_length - len(parentesco_titular))

        if socio.isdigit() and valor_mes.isdigit() and numero_meses.isdigit():
                print('llegue crear poliza')
                fecha_afiliacion = datetime.now().date()
                print(fecha_afiliacion)
                hora_actual = datetime.now().strftime('%H:%M:%S')
                print(hora_actual)
                hasta_fecha = fecha_afiliacion + relativedelta(months=int(numero_meses))
                print(hasta_fecha)
                valor_total = int(valor_mes) * int(numero_meses)
                print(valor_total)
                print(documentos)

                documentos_int = []
                nombres_int = []
                parentesco_int=[]

                for elemento in documentos:
                    # Verificar si el elemento es de tipo texto (str) y no está vacío
                    if isinstance(elemento, str) and elemento.strip():  # Verificar que no esté vacío
                        # Si es de tipo texto y no está vacío, convertir el elemento a entero y agregar a la lista documentos_int
                        documentos_int.append(int(elemento))
                    else:
                        # Si es de tipo texto y está vacío, agregar 000 a la lista documentos_int como entero
                        documentos_int.append(000)

                nombres_str = '{{{}}}'.format(
                    ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombres))))
                parentesco_titular_str = '{{{}}}'.format(
                    ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, parentesco_titular))))

                fechas_nacimiento = ['01/01/2000' if fecha == valor_por_defecto else fecha for fecha in
                                     fechas_nacimiento]

                fechas_nacimiento_int = [datetime.strptime(elemento, "%d/%m/%Y").date() for elemento in fechas_nacimiento]
                fechas_afiliacion = [datetime.now().date() for _ in range(len(documentos_int))]
                print(fechas_afiliacion)
                print(fechas_nacimiento_int)
                mayor_70 = []
                for fecha_nacimiento, fecha_afiliacion in zip(fechas_nacimiento_int, fechas_afiliacion):
                    diferencia = fecha_afiliacion - fecha_nacimiento
                    edad = diferencia.days // 365  # Aproximación de la edad en años

                    if edad >= 70:
                        mayor_70.append(True)
                    else:
                        mayor_70.append(False)

                # Imprime la lista mayor_70
                print(mayor_70)

                try:
                    with conexion.cursor() as cursor:
                        consulta = "INSERT INTO polizas(socio, nombres, documentos, fechas_nacimiento, parentesco_titular, fecha_afiliacion, mayor_70, estado, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago, fecha_desde, fecha_hasta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(consulta, (int(socio), nombres_str, documentos_int, fechas_nacimiento_int, parentesco_titular_str, fechas_afiliacion, mayor_70, True, int(valor_total), usuario_encargado, usuario_encargado, fecha_afiliacion,fecha_afiliacion, hasta_fecha ))
                    conexion.commit()
                    print("Poliza ingresada")
                    try:
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            cursor.execute(consulta, (int(valor_mes), fecha_afiliacion, hasta_fecha, fecha_afiliacion, hora_actual, usuario_encargado, documentos_int, nombres_str, int(socio), False))
                        conexion.commit()
                        print("Colilla creada")

                        try:
                            with conexion.cursor() as cursor:
                                cursor.execute(
                                    """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                ultimo_dato_insertado = cursor.fetchone()
                                print(ultimo_dato_insertado)


                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (socio, valor_total, fecha_afiliacion, ultimo_dato_insertado[6], ultimo_dato_insertado[7], ultimo_dato_insertado[8], int(ultimo_dato_insertado[9]) + (int(valor_total)/2), int(ultimo_dato_insertado[10]) + ((valor_total)/2), int(ultimo_dato_insertado[11]) + valor_total, False))
                                    conexion.commit()
                                print("Saldo cambiado")
                                pdf_colilla(datetime.now().date(),socio, valor_total, datetime.now().date(), hasta_fecha, usuario_encargado, nombres[0],documentos[0] )
                                return "Todo generado con exito"

                            except psycopg2.Error as e:
                                return ("Ocurrió un error al crear el ultimo saldo:"+  str(e))
                        except psycopg2.Error as e:
                                return ("Ocurrió un error al seleccionar el ultimo:"+  str(e))
                    except psycopg2.Error as e:
                        return ("Ocurrió un error al crear la colilla"+  str(e))
                except psycopg2.Error as e:
                    return "Ocurrió un error al crear la poliza" + str(e)

        else:
            return "No es un número de socio, valor o numero de meses correcto"

    def eliminar_persona(self, socio, nombre_par, documento_par, fecha_nacimiento_par, parentesco_par):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM polizas WHERE socio=" + str(socio))
                poliza = cursor.fetchone()

                if poliza:
                    documentos_poliza = poliza[2] or []
                    nombres_poliza = poliza[1] or []
                    fechas_nacimiento = poliza[3] or []
                    parentesco_titular = poliza[4] or []
                    fecha_afiliacion = poliza[5]
                    mayor_70 = poliza[6] or []

                    if int(documento_par) in documentos_poliza and nombre_par in nombres_poliza:
                        # Filtrar por coincidencia de documento y nombre
                        documentos_poliza = [doc for doc, nombre in zip(documentos_poliza, nombres_poliza) if
                                             doc != int(documento_par) or nombre != nombre_par]
                        nombres_poliza = [nombre for nombre in nombres_poliza if nombre != nombre_par]
                        fechas_nacimiento = [fecha for fecha, nombre in zip(fechas_nacimiento, nombres_poliza) if
                                             nombre != nombre_par]
                        parentesco_titular = [parentesco for parentesco, nombre in
                                              zip(parentesco_titular, nombres_poliza)
                                              if nombre != nombre_par]
                        fecha_afiliacion = [fecha for fecha, nombre in zip(fecha_afiliacion, nombres_poliza) if
                                            nombre != nombre_par]
                        mayor_70 = [mayor for mayor, nombre in zip(mayor_70, nombres_poliza) if nombre != nombre_par]

                        # Actualizar la base de datos
                        actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s, parentesco_titular=%s ,fecha_afiliacion=%s, mayor_70=%s WHERE socio=%s"
                        cursor.execute(actualizacion, (
                            documentos_poliza, nombres_poliza, fechas_nacimiento, parentesco_titular, fecha_afiliacion,
                            mayor_70, int(socio)))
                        conexion.commit()

                        return "El documento y los datos correspondientes han sido eliminados correctamente."

                    else:
                        return "El documento no se encontraba en la lista."
                else:
                    return "La póliza no existe."

        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: {}".format(e)

    def agregar_persona_poliza(self, socio, nuevo_documentor, nuevo_nombre, nueva_fecha_nacimiento, parentesco_titular,
                               nuevo_valor):
        print(socio,nuevo_documentor,nuevo_nombre,nueva_fecha_nacimiento,parentesco_titular,nuevo_valor)
        socio = str(socio) if socio is not None else ''
        nuevo_documento = int(nuevo_documentor) if nuevo_documentor != '' else 0

        if socio.isdigit() and nuevo_valor.isdigit():
            fecha_afiliacion = datetime.now().date()
            print('Entre a la función')
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM polizas WHERE socio=" + str(socio))
                    poliza = cursor.fetchone()
                    print(poliza)

                    if poliza:
                        # Obtener las listas existentes en la fila
                        documentos_poliza = poliza[2]
                        nombres_poliza = poliza[1]
                        fechas_nacimiento = poliza[3]
                        parentescos_titular = poliza[4]
                        fechas_afiliacion = poliza[-9]
                        mayor_70 = poliza[-8]

                        # Convertir la fecha de string a objeto de fecha
                        nueva_fecha_nacimiento = datetime.strptime(nueva_fecha_nacimiento, '%d/%m/%Y').date()
                        diferencia = fecha_afiliacion - nueva_fecha_nacimiento
                        edad = diferencia.days // 365  # Aproximación de la edad en años

                        if edad >= 70:
                            mayor_70.append(True)
                        else:
                            mayor_70.append(False)

                        fechas_afiliacion.append(datetime.now().date())
                        documentos_poliza.append((nuevo_documento))
                        nombres_poliza.append(nuevo_nombre)
                        fechas_nacimiento.append(nueva_fecha_nacimiento)
                        parentescos_titular.append(parentesco_titular)
                        actualizacion = "UPDATE polizas SET mayor_70=%s, documentos=%s, nombres=%s, fechas_nacimiento=%s, parentesco_titular=%s, valor_mes=%s, fecha_afiliacion=%s WHERE socio=%s"
                        cursor.execute(actualizacion, (
                            mayor_70, documentos_poliza, nombres_poliza, fechas_nacimiento, parentescos_titular, int(nuevo_valor),
                            fechas_afiliacion, int(socio)))

                        conexion.commit()

                        return "Los datos han sido agregados correctamente."
                    else:
                        return "El socio no existe en la tabla."
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "No es un número de socio o nuevo valor correctos"

    def marcar_persona_fallecida (self, socio, documento, nuevo_valor):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM polizas WHERE socio=" + str(socio))
                poliza = cursor.fetchone()
                documentos_poliza = poliza[2]
                nombres_poliza = poliza[1]
                fechas_nacimiento = poliza[3]
                parentesco_titular = poliza[4]
                fecha_afiliacion = poliza[5]
                mayor_70 = poliza[6]

                if documentos_poliza:
                    print(documentos_poliza)

                    # Verificar si el documento existe en la lista
                    if documento in documentos_poliza:
                        # Obtener la posición del documento en la lista
                        posicion = documentos_poliza.index(documento)

                        documentos_poliza.pop(posicion)
                        nombres_poliza.pop(posicion)
                        fechas_nacimiento.pop(posicion)
                        parentesco_titular.pop(posicion)
                        fecha_afiliacion.pop(posicion)
                        mayor_70.pop(posicion)

                        actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s, valor_mes=%s WHERE socio=%s"
                        cursor.execute(actualizacion, (documentos_poliza, nombres_poliza, fechas_nacimiento,nuevo_valor, socio))
                        conexion.commit()

                        print("El documento y los datos correspondientes han sido eliminados correctamente.")
                    else:
                        print("El documento no se encontraba en la lista.")
                else:
                    print("La póliza no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar:", e)

    def consultar_poliza_socio(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, mayor_70, fecha_afiliacion FROM polizas WHERE socio=" + str(socio))
                    poliza = cursor.fetchone()
                    print(poliza)
                    if poliza != None:

                        return poliza
                    else:
                        return 'No se encuentra ninguna poliza'
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar:", e)
        else:
            return "No es un número de socio correcto"

    def consultar_poliza_socio_mod(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, parentesco_titular FROM polizas WHERE socio=" + str(socio))
                    poliza = cursor.fetchone()
                    print(poliza)
                    if poliza != None:

                        return poliza
                    else:
                        return 'No se encuentra ninguna poliza'
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar:", e)
        else:
            return "No es un número de socio correcto"

    def consultar_poliza_documento(self, documento):
        print(documento)
        if documento.isdigit():
            try:
                documento_entero = int(documento)
                print(documento_entero)
                with conexion.cursor() as cursor:
                    consulta = "SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, mayor_70, socio FROM polizas WHERE %s = ANY (documentos)"
                    cursor.execute(consulta, (documento_entero,))
                    polizas = cursor.fetchall()
                    if polizas:
                        print(polizas)
                        return polizas
                    else:
                        print("No te encuentras en ninguna póliza")
                        return 'No se encontró en ninguna póliza'
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            print(documento)
            return "No es un número de documento correcto"


    def modificar_poliza(self, socio, nombres, documentos, fechas_nacimiento, parentesco_titular, valor_mes):
        print('entre')
        print(socio)
        print(nombres)
        print(documentos)
        print(fechas_nacimiento)
        print(parentesco_titular)
        print(valor_mes)

        documentos_int = [int(elemento) for elemento in documentos]

        fechas_nacimiento_date = []
        for elemento in fechas_nacimiento:
            try:
                # Verificar si la fecha ya está en formato "%Y-%m-%d"
                if "-" in elemento:
                    fecha = datetime.strptime(elemento, "%Y-%m-%d").date()
                else:
                    fecha = datetime.strptime(elemento, "%d/%m/%Y").date()

                fechas_nacimiento_date.append(fecha)
            except ValueError:
                print(f"Error al convertir la fecha: {elemento}")

        print('voy a intentar modificar base')

        try:
            with conexion.cursor() as cursor:
                actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s, parentesco_titular=%s, valor_mes=%s WHERE socio=%s"
                cursor.execute(actualizacion, (
                    documentos_int, nombres, fechas_nacimiento_date, parentesco_titular, int(valor_mes), int(socio)))
                conexion.commit()
            return "Todo generado con éxito"
        except psycopg2.Error as e:
            print("Ocurrió un error al modificar la póliza: " + str(e))
            return "Ocurrió un error al modificar la póliza: " + str(e)

    def crear_poliza_antigua (self, socio, nombres, documentos, fechas_nacimiento, parentesco_titular, valor_mes, numero_meses, usuario_encargado,  fecha_desdef, fecha_afiliacion):

        valor_por_defecto = ''

        # Encuentra la longitud máxima entre las listas
        max_length = max(len(nombres), len(documentos), len(fechas_nacimiento), len(parentesco_titular))

        # Rellena o recorta las listas para que tengan la misma longitud
        nombres = list(nombres) + [valor_por_defecto] * (max_length - len(nombres))
        documentos = list(documentos) + [valor_por_defecto] * (max_length - len(documentos))
        fechas_nacimiento = list(fechas_nacimiento) + [valor_por_defecto] * (max_length - len(fechas_nacimiento))
        parentesco_titular = list(parentesco_titular) + [valor_por_defecto] * (max_length - len(parentesco_titular))

        print(valor_mes, numero_meses)
        if valor_mes.isdigit() and numero_meses.isdigit():

            hora_actual = datetime.now().strftime('%H:%M:%S')

            fecha_desde = datetime.strptime(fecha_desdef, '%d/%m/%Y')
            hasta_fecha = fecha_desde + relativedelta(months=int(numero_meses))

            valor_total = int(valor_mes) * int(numero_meses)

            documentos_int = []

            for elemento in documentos:
                # Verificar si el elemento es de tipo texto (str) y no está vacío
                if isinstance(elemento, str) and elemento.strip():  # Verificar que no esté vacío

                    # Si es de tipo texto y no está vacío, convertir el elemento a entero y agregar a la lista documentos_int
                    try:

                        documentos_int.append(int(elemento))
                    except:
                        return "no es documento"
                else:
                    # Si es de tipo texto y está vacío, agregar 000 a la lista documentos_int como entero
                    documentos_int.append(000)

            nombres_str = '{{{}}}'.format(
                ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombres))))
            parentesco_titular_str = '{{{}}}'.format(
                ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, parentesco_titular))))

            fechas_nacimiento = ['01/01/2000' if fecha == valor_por_defecto else fecha for fecha in fechas_nacimiento]

            # Convierte las fechas a objetos datetime
            fechas_nacimiento_int = [datetime.strptime(elemento, "%d/%m/%Y").date() for elemento in fechas_nacimiento]
            fechas_afiliacion_str = [fecha_afiliacion for _ in range(len(documentos_int))]

            mayor_70 = []
            fechas_afiliacion = [datetime.strptime(fecha, '%d/%m/%Y').date() for fecha in fechas_afiliacion_str]
            for fecha_nacimiento, fecha_afiliacion in zip(fechas_nacimiento_int, fechas_afiliacion):
                diferencia = fecha_afiliacion - fecha_nacimiento
                edad = diferencia.days // 365  # Aproximación de la edad en años

                if edad >= 70:
                    mayor_70.append(True)
                else:
                    mayor_70.append(False)

            # Imprime la lista mayor_70
            print(mayor_70)
            fecha_actual = datetime.now().date()
            try:
                with conexion.cursor() as cursor:
                    # Verificar si el socio ya existe
                    consulta_verificacion = "SELECT COUNT(*) FROM polizas WHERE socio = %s;"
                    cursor.execute(consulta_verificacion, (int(socio),))
                    resultado = cursor.fetchone()

                    # Si el socio no existe, proceder con la inserción
                    if resultado[0] == 0:
                        try:
                            with conexion.cursor() as cursor:
                                consulta = "INSERT INTO polizas(socio, nombres, documentos, fechas_nacimiento, parentesco_titular, fecha_afiliacion, mayor_70, estado, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago, fecha_desde, fecha_hasta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                cursor.execute(consulta, (
                                    int(socio), nombres_str, documentos_int, fechas_nacimiento_int, parentesco_titular_str,
                                    fechas_afiliacion, mayor_70, True, valor_mes, usuario_encargado, usuario_encargado,
                                    fecha_actual, fecha_desde, hasta_fecha))
                            conexion.commit()
                            print("Poliza ingresada")
                            try:
                                with conexion.cursor() as cursor:
                                    consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                    cursor.execute(consulta, (int(valor_mes), fecha_desde, hasta_fecha, fecha_actual, hora_actual,
                                        usuario_encargado,documentos_int, nombres_str, int(socio), False))
                                conexion.commit()
                                print("Colilla creada")

                                try:
                                    with conexion.cursor() as cursor:
                                        cursor.execute(
                                            """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                        ultimo_dato_insertado = cursor.fetchone()
                                        print(ultimo_dato_insertado)

                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (
                                                socio, valor_total, fecha_actual, ultimo_dato_insertado[6],
                                                ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                                int(ultimo_dato_insertado[9]) + (int(valor_total) / 2),
                                                int(ultimo_dato_insertado[10]) + ((valor_total) / 2),
                                                int(ultimo_dato_insertado[11]) + valor_total, False))
                                            conexion.commit()
                                        print("Saldo cambiado")
                                        pdf_colilla(datetime.now().date(), socio, valor_total, fecha_desde.date(), hasta_fecha.date(), usuario_encargado, nombres[0], documentos[0])
                                        return "Todo generado con exito"
                                    except psycopg2.Error as e:
                                        return ("Ocurrió un error al crear el ultimo saldo:" + str(e))
                                except psycopg2.Error as e:
                                    return ("Ocurrió un error al seleccionar el ultimo:" + str(e))
                            except psycopg2.Error as e:
                                return ("Ocurrió un error al crear la colilla" + str(e))
                        except psycopg2.Error as e:
                            return "Ocurrió un error al crear la poliza" + str(e)
                    else:
                        return ("El socio ya existe en la base de datos. No se realizó la inserción.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            return "No es un número de socio, valor o numero de meses correcto"



















