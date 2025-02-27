from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Front.generar_pdfs import pdf_colilla, generar_pdf_proexequial
import psycopg2.extras
from itertools import zip_longest
from array import array

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Polizas ():

    def crear_poliza (self, socio, nombres, documentos, fechas_nacimiento, valor_mes, numero_meses, usuario_encargado, nota, telefono):

            valor_por_defecto = ''
            print(nombres)

            # Encuentra la longitud máxima entre las listas
            max_length = max(len(nombres), len(documentos), len(fechas_nacimiento))

            print(nombres)

            # Rellena o recorta las listas para que tengan la misma longitud
            nombresl = list(nombres) + [valor_por_defecto] * (max_length - len(nombres))
            print(nombresl)
            documentos = list(documentos) + [valor_por_defecto] * (max_length - len(documentos))
            fechas_nacimiento = list(fechas_nacimiento) + [valor_por_defecto] * (max_length - len(fechas_nacimiento))

            if socio.isdigit() and valor_mes.isdigit() and numero_meses.isdigit():
                    print('llegue crear poliza')
                    fecha_afiliacion = datetime.now().date()
                    print(fecha_afiliacion)
                    hora_actual = datetime.now().strftime('%H:%M:%S')
                    print(hora_actual)
                    hasta_fecha = fecha_afiliacion + relativedelta(months=int(numero_meses))
                    print(hasta_fecha)


                    hasta_fecha_str = hasta_fecha.strftime("%Y-%m-%d")
                    print("Fecha en formato de cadena:", hasta_fecha_str)

                    # Convertir la cadena a un objeto datetime
                    hasta_fecha_dat = datetime.strptime(hasta_fecha_str, "%Y-%m-%d")
                    print("Fecha como objeto datetime:", hasta_fecha_dat)
                    print(hasta_fecha_dat)
                    fecha_comparacion = datetime(2026, 1, 10)
                    print(fecha_comparacion)
                    if hasta_fecha_dat < fecha_comparacion:






                        valor_total = int(valor_mes) * int(numero_meses)
                        print(valor_total)
                        print(documentos)

                        documentos_int = []

                        for elemento in documentos:
                            # Verificar si el elemento es de tipo texto (str) y no está vacío
                            if isinstance(elemento, str) and elemento.strip():  # Verificar que no esté vacío

                                # Si es de tipo texto y no está vacío, convertir el elemento a entero y agregar a la lista documentos_int
                                try:

                                    documentos_int.append(int(elemento))
                                except:
                                    return "No es un documento"
                            else:
                                # Si es de tipo texto y está vacío, agregar 000 a la lista documentos_int como entero
                                documentos_int.append(000)





                        nombres_str = '{{{}}}'.format(
                            ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombresl))))
                       

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
                                # Verificar si el socio ya existe
                                consulta_verificacion = "SELECT COUNT(*) FROM polizas WHERE socio = %s;"
                                cursor.execute(consulta_verificacion, (int(socio),))
                                resultado = cursor.fetchone()

                                # Si el socio no existe, proceder con la inserción
                                if resultado[0] == 0:

                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO polizas(socio, nombres, documentos, fechas_nacimiento, fecha_afiliacion, mayor_70, estado, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago, fecha_desde, fecha_hasta, nota_poliza, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (int(socio), nombres_str, documentos_int, fechas_nacimiento_int, fechas_afiliacion, mayor_70, True, int(valor_mes), usuario_encargado, usuario_encargado, fecha_afiliacion,fecha_afiliacion, hasta_fecha, nota, (telefono) ))
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
                                                        consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                        cursor.execute(consulta, (socio, valor_total, fecha_afiliacion, ultimo_dato_insertado[6], ultimo_dato_insertado[7], ultimo_dato_insertado[8], int(ultimo_dato_insertado[9]) + (int(valor_total)/2), int(ultimo_dato_insertado[10]) + ((valor_total)/2), int(ultimo_dato_insertado[11]) + valor_total, False, ''))
                                                        conexion.commit()
                                                    print("Saldo cambiado")
                                                    generar_pdf_proexequial(datetime.now().date(), documentos_int, nombresl, fechas_nacimiento_int, fechas_afiliacion, socio, "La Unión Antioquia")
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
                                    return ("El socio ya existe en la base de datos. No se realizó la inserción.")
                        except Exception as e:
                            return (f"Error: {e}")
                    else:
                        print("Fecha hasta no es menor que 10/01/2026")
                        return "Fecha hasta no es menor que 10/01/2026"
            else:
                return "El socio, el valor del mes y el número de meses, deben ser unicamente números"

    def eliminar_persona(self, socio, nombre_par, documento_par, fecha_nacimiento_par):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM polizas WHERE socio=" + str(socio))
                poliza = cursor.fetchone()

                if poliza:
                    documentos_poliza = poliza[2] or []
                    nombres_poliza = poliza[1] or []
                    fechas_nacimiento = poliza[3] or []
                    fecha_afiliacion = poliza[5]
                    mayor_70 = poliza[6] or []

                    if int(documento_par) in documentos_poliza and nombre_par in nombres_poliza:
                        # Filtrar por coincidencia de documento y nombre
                        documentos_poliza = [doc for doc, nombre in zip(documentos_poliza, nombres_poliza) if
                                             doc != int(documento_par) or nombre != nombre_par]
                        nombres_poliza = [nombre for nombre in nombres_poliza if nombre != nombre_par]
                        fechas_nacimiento = [fecha for fecha, nombre in zip(fechas_nacimiento, nombres_poliza) if
                                             nombre != nombre_par]
                        fecha_afiliacion = [fecha for fecha, nombre in zip(fecha_afiliacion, nombres_poliza) if
                                            nombre != nombre_par]
                        mayor_70 = [mayor for mayor, nombre in zip(mayor_70, nombres_poliza) if nombre != nombre_par]

                        # Actualizar la base de datos
                        actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s,fecha_afiliacion=%s, mayor_70=%s WHERE socio=%s"
                        cursor.execute(actualizacion, (
                            documentos_poliza, nombres_poliza, fechas_nacimiento, fecha_afiliacion,
                            mayor_70, int(socio)))
                        conexion.commit()
                        #generar_pdf_proexequial(datetime.now().date(), documentos_poliza, nombres_poliza, fechas_nacimiento, fecha_afiliacion, socio, "La Unión Antioquia")

                        return "El documento y los datos correspondientes han sido eliminados correctamente."

                    else:
                        return "El documento no se encontraba en la lista."
                else:
                    return "La póliza no existe."

        except psycopg2.Error as e:
            return "Ocurrió un error al consultar: {}".format(e)

    def agregar_persona_poliza(self, socio, nuevo_documentor, nuevo_nombre, nueva_fecha_nacimiento,
                               nuevo_valor):
        if socio.isdigit() and nuevo_valor.isdigit():
            print(socio,nuevo_documentor,nuevo_nombre,nueva_fecha_nacimiento,nuevo_valor)
            socio = str(socio) if socio is not None else ''
            nuevo_documento = int(nuevo_documentor) if nuevo_documentor != '' else 0


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
                        fechas_afiliacion = poliza[5]
                        mayor_70 = poliza[6]

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
                        actualizacion = "UPDATE polizas SET mayor_70=%s, documentos=%s, nombres=%s, fechas_nacimiento=%s, valor_mes=%s, fecha_afiliacion=%s WHERE socio=%s"
                        cursor.execute(actualizacion, (
                            mayor_70, documentos_poliza, nombres_poliza, fechas_nacimiento, int(nuevo_valor),
                            fechas_afiliacion, int(socio)))

                        conexion.commit()
                        generar_pdf_proexequial(datetime.now().date(), documentos_poliza, nombres_poliza, fechas_nacimiento, fechas_afiliacion, socio, "La Unión Antioquia")

                        return "Los datos han sido agregados correctamente."
                    else:
                        return "El socio no existe en la tabla."
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "El socio, el documento y el nuevo valor deben ser números"

    def consultar_poliza_socio(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, mayor_70, fecha_afiliacion, parentesco_titular, nota_poliza, telefono FROM polizas WHERE socio=" + str(socio))
                    poliza = cursor.fetchone()
                    print(poliza)
                    if poliza != None:

                        return poliza
                    else:
                        return 'No se encuentra ninguna poliza'
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar:", e)
        else:
            return "El socio debe ser un número"

    def consultar_poliza_socio_mod(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, parentesco_titular, nota_poliza, telefono FROM polizas WHERE socio=" + str(socio))
                    poliza = cursor.fetchone()
                    print(poliza)
                    if poliza != None:

                        return poliza
                    else:
                        return 'No se encuentra ninguna poliza'
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar:", e)
        else:
            return "El socio debe ser un número"

    def consultar_poliza_documento(self, documento):
        print(documento)
        if documento.isdigit():
            try:
                documento_entero = int(documento)
                print(documento_entero)
                with conexion.cursor() as cursor:
                    consulta = "SELECT valor_mes, fecha_desde, fecha_hasta, nombres, documentos, fechas_nacimiento, mayor_70, socio, fecha_afiliacion, parentesco_titular, nota_poliza, telefono FROM polizas WHERE %s = ANY (documentos)"
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
            return "El documento debe ser un número"

    def modificar_poliza(self, socio, nombres, documentos, fechas_nacimiento, valor_mes, nota, telefono):
        if all(x.isdigit() for x in documentos) and valor_mes.isdigit() and socio.isdigit:
            print('entre')
            print(socio)
            print(nombres)
            print(documentos)
            print(fechas_nacimiento)
            print(valor_mes)
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT fecha_afiliacion FROM polizas WHERE socio=" + str(socio))
                    fechas_afiliacion = cursor.fetchone()
                    print(fechas_afiliacion)
                    if fechas_afiliacion != None:

                        print( fechas_afiliacion)
                    else:
                        return 'No se encuentra ninguna poliza'
            except psycopg2.Error as e:
                return ("Ocurrió un error al consultar:", e)

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
                    actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s, valor_mes=%s, nota_poliza=%s, telefono=%s WHERE socio=%s"
                    cursor.execute(actualizacion, (
                        documentos_int, nombres, fechas_nacimiento_date, int(valor_mes), str(nota), str(telefono),int(socio)))
                    conexion.commit()
                generar_pdf_proexequial(datetime.now().date(), documentos, nombres, fechas_nacimiento_date, fechas_afiliacion[0], socio, "La Unión Antioquia")

                return "Todo generado con éxito"
            except psycopg2.Error as e:
                print("Ocurrió un error al modificar la póliza: " + str(e))
                return "Ocurrió un error al modificar la póliza: " + str(e)
        else:
            return "Los documentos, el valor del mes y el socio deben ser números"

    def crear_poliza_antigua (self, socio, nombres, documentos, fechas_nacimiento, valor_mes, numero_meses, usuario_encargado,  fecha_desdef, fecha_afiliacion, nota, telefono):

            valor_por_defecto = ''

            # Encuentra la longitud máxima entre las listas
            max_length = max(len(nombres), len(documentos), len(fechas_nacimiento))

            # Rellena o recorta las listas para que tengan la misma longitud
            nombresl = list(nombres) + [valor_por_defecto] * (max_length - len(nombres))
            documentos = list(documentos) + [valor_por_defecto] * (max_length - len(documentos))
            fechas_nacimiento = list(fechas_nacimiento) + [valor_por_defecto] * (max_length - len(fechas_nacimiento))


            if valor_mes.isdigit() and numero_meses.isdigit() and socio.isdigit():

                hora_actual = datetime.now().strftime('%H:%M:%S')

                fecha_desde = datetime.strptime(fecha_desdef, '%d/%m/%Y')
                hasta_fecha = fecha_desde + relativedelta(months=int(numero_meses))


                hasta_fecha_str = hasta_fecha.strftime("%Y-%m-%d")
                print("Fecha en formato de cadena:", hasta_fecha_str)

                # Convertir la cadena a un objeto datetime
                hasta_fecha_dat = datetime.strptime(hasta_fecha_str, "%Y-%m-%d")
                print("Fecha como objeto datetime:", hasta_fecha_dat)
                print(hasta_fecha_dat)
                fecha_comparacion = datetime(2025, 1, 10)
                fecha_comparacion2 = datetime(2026, 1, 10)
                print(fecha_comparacion)
                
                if fecha_comparacion2 > hasta_fecha_dat:
                    if hasta_fecha_dat < fecha_comparacion:






                        valor_total = int(valor_mes) * int(numero_meses)
                        print(valor_total)
                        print(documentos)

                        documentos_int = []

                        for elemento in documentos:
                            # Verificar si el elemento es de tipo texto (str) y no está vacío
                            if isinstance(elemento, str) and elemento.strip():  # Verificar que no esté vacío

                                # Si es de tipo texto y no está vacío, convertir el elemento a entero y agregar a la lista documentos_int
                                try:

                                    documentos_int.append(int(elemento))
                                except:
                                    return "No es un documento"
                            else:
                                # Si es de tipo texto y está vacío, agregar 000 a la lista documentos_int como entero
                                documentos_int.append(000)





                        nombres_str = '{{{}}}'.format(
                            ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombresl))))

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
                                # Verificar si el socio ya existe
                                consulta_verificacion = "SELECT COUNT(*) FROM polizas WHERE socio = %s;"
                                cursor.execute(consulta_verificacion, (int(socio),))
                                resultado = cursor.fetchone()

                                # Si el socio no existe, proceder con la inserción
                                if resultado[0] == 0:

                                    try:
                                        with conexion.cursor() as cursor:
                                            consulta = "INSERT INTO polizas(socio, nombres, documentos, fechas_nacimiento, fecha_afiliacion, mayor_70, estado, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago, fecha_desde, fecha_hasta, nota_poliza, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (int(socio), nombres_str, documentos_int, fechas_nacimiento_int, fechas_afiliacion, mayor_70, True, int(valor_mes), usuario_encargado, usuario_encargado, fecha_afiliacion,fecha_afiliacion, hasta_fecha, nota, telefono ))
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
                                                        consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                        cursor.execute(consulta, (socio, valor_total, fecha_afiliacion, ultimo_dato_insertado[6], ultimo_dato_insertado[7], ultimo_dato_insertado[8], int(ultimo_dato_insertado[9]) + (int(valor_total)/2), int(ultimo_dato_insertado[10]) + ((valor_total)/2), int(ultimo_dato_insertado[11]) + valor_total, False, ''))
                                                        conexion.commit()
                                                    print("Saldo cambiado")
                                                    generar_pdf_proexequial(datetime.now().date(), documentos_int, nombresl, fechas_nacimiento_int, fechas_afiliacion, socio, "La Unión Antioquia")
                                                    pdf_colilla(datetime.now().date(),socio, valor_total, fecha_desde.date(), hasta_fecha, usuario_encargado, nombres[0],documentos[0] )
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
                                    return ("El socio ya existe en la base de datos. No se realizó la inserción.")
                        except Exception as e:
                            return (f"Error: {e}")
                    else:
                        valor_mes_antiguo = int(valor_mes)
                        valor_mes_nuevo = int(valor_mes) + (int(len(nombres))*500)
        
                        # Fecha de referencia para el cambio de precio
                        fecha_cambio_precio = datetime(2024, 12, 10).date()  # Convertimos a date
        
                        valor_total = 0
        
                        # Recorremos cada mes para determinar el costo
                        for mes in range(int(numero_meses)):
                            # Calcula la fecha actual sumando meses (como datetime.date)
                            fecha_actual = fecha_desde + relativedelta(months=mes)
                            if fecha_actual.date() <= fecha_cambio_precio:
                                valor_total += valor_mes_antiguo
                            else:
                                valor_total += valor_mes_nuevo
        
                        print(f"El valor total a pagar es: {valor_total}")
                        documentos_int = []
    
                        for elemento in documentos:
                            # Verificar si el elemento es de tipo texto (str) y no está vacío
                            if isinstance(elemento, str) and elemento.strip():  # Verificar que no esté vacío
    
                                # Si es de tipo texto y no está vacío, convertir el elemento a entero y agregar a la lista documentos_int
                                try:
    
                                    documentos_int.append(int(elemento))
                                except:
                                    return "No es un documento"
                            else:
                                # Si es de tipo texto y está vacío, agregar 000 a la lista documentos_int como entero
                                documentos_int.append(000)
    
                        nombres_str = '{{{}}}'.format(
                            ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombres))))

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
                                            consulta = "INSERT INTO polizas(socio, nombres, documentos, fechas_nacimiento, fecha_afiliacion, mayor_70, estado, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago, fecha_desde, fecha_hasta, nota_poliza, suba_anual, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                            cursor.execute(consulta, (
                                                int(socio), nombres_str, documentos_int, fechas_nacimiento_int,
                                                fechas_afiliacion, mayor_70, True, valor_mes_nuevo, usuario_encargado, usuario_encargado,
                                                fecha_actual, fecha_desde, hasta_fecha, nota, True, telefono))
                                        conexion.commit()
                                        print("Poliza ingresada")
                                        try:
                                            with conexion.cursor() as cursor:
                                                consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                cursor.execute(consulta, (int(valor_mes_nuevo), fecha_desde, hasta_fecha, fecha_actual, hora_actual,
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
                                                        consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                        cursor.execute(consulta, (
                                                            socio, valor_total, fecha_actual, ultimo_dato_insertado[6],
                                                            ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                                            int(ultimo_dato_insertado[9]) + (int(valor_total) / 2),
                                                            int(ultimo_dato_insertado[10]) + ((valor_total) / 2),
                                                            int(ultimo_dato_insertado[11]) + valor_total, False, ''))
                                                        conexion.commit()
                                                    print("Saldo cambiado")
                                                    generar_pdf_proexequial(datetime.now().date(), documentos_int, nombresl, fechas_nacimiento_int, fechas_afiliacion, socio, "La Unión Antioquia")
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
                            return (f"Error parte de la suba: {e}")    
                else:
                    return ("Excede la fecha límite 10/01/2026")
            else:
                return "El valor del mes, el número de meses, y el socio deben ser unicamente números"



















