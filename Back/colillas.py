from BD.Conexion import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Front.generar_pdfs import pdf_colilla
from datetime import datetime
from datetime import datetime, timedelta


basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion= basedatos.conectar()

class Colillas ():
    
    def crear_colilla_socio(self, socio, numero_meses, usuario_encargado):
       if socio.isdigit() and numero_meses.isdigit():
           print('esta raro')
           self.hora_actual = datetime.now().strftime('%H:%M:%S')
           self.fecha_actual = datetime.now().date()

           try:
               with conexion.cursor() as cursor:
                   cursor.execute("SELECT * FROM polizas WHERE socio=" + str(socio))
                   poliza = cursor.fetchone()
                   if poliza:
                       suba_anual = poliza[15]
                       hasta_fecha = poliza [9] + relativedelta(months=int(numero_meses))
                       print(hasta_fecha)
                       hasta_fecha_str = hasta_fecha.strftime("%Y-%m-%d")
                       print("Fecha en formato de cadena:", hasta_fecha_str)

                       # Convertir la cadena a un objeto datetime
                       hasta_fecha_dat = datetime.strptime(hasta_fecha_str, "%Y-%m-%d")
                       print("Fecha como objeto datetime:", hasta_fecha_dat)
                       print(hasta_fecha_dat)
                       fecha_comparacion = datetime(2025, 1, 10)
                       fecha_comparacion2 = datetime(2026, 1, 10)

                       print(fecha_comparacion)
                       
                       
                       if hasta_fecha_dat < fecha_comparacion2:
                       
                       
                       
                           if hasta_fecha_dat < fecha_comparacion:
                               print("hasta_fecha es menor que 10/01/2025")
                               try:
                                   with conexion.cursor() as cursor:
                                       consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                       cursor.execute(consulta, (
                                           poliza[10], poliza[9], hasta_fecha, self.fecha_actual, self.hora_actual,
                                           usuario_encargado,
                                           poliza[2], poliza[1], int(socio), False))
                                   conexion.commit()
                                   print("Colilla creada")
    
                                   try:
                                       with conexion.cursor() as cursor:
                                           cursor.execute(
                                               """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                           ultimo_dato_insertado = cursor.fetchone()
                                           print(ultimo_dato_insertado)
                                       try:
                                           valor_total = int(poliza[10]) * int(numero_meses)
                                           with conexion.cursor() as cursor:
                                               consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                               cursor.execute(consulta, (
                                               socio, valor_total, self.fecha_actual, ultimo_dato_insertado[6],
                                               ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                               ultimo_dato_insertado[9] + ((valor_total) / 2),
                                               ultimo_dato_insertado[10] + (valor_total / 2),
                                               ultimo_dato_insertado[11] + valor_total, False, ''))
                                           conexion.commit()
                                           print("Saldo cambiado")
    
                                           try:
                                               with conexion.cursor() as cursor:
                                                   consulta = "UPDATE polizas SET fecha_desde = %s, fecha_hasta = %s, usuario_ultimo_pago = %s, fecha_ultimo_pago = %s WHERE socio = %s"
                                                   cursor.execute(consulta,
                                                                  (poliza[9], hasta_fecha, usuario_encargado,
                                                                   self.fecha_actual, socio))
                                               conexion.commit()
    
    
                                               pdf_colilla(self.fecha_actual, socio, valor_total, poliza[9], hasta_fecha,
                                                           usuario_encargado, poliza[1][0], poliza[2][0])
    
                                               print("Todos los datos de la colilla se han cambiado correctamente")
                                               return "Todos los datos de la colilla se han cambiado correctamente"
                                           except psycopg2.Error as e:
    
                                               return "Ocurrió un error al editar: " + str(e)
                                       except psycopg2.Error as e:
                                           return ("Ocurrió un error al crear el ultimo saldo:" + str(e))
                                   except psycopg2.Error as e:
                                       return ("Ocurrió un error al seleccionar el ultimo:" + str(e))
                               except psycopg2.Error as e:
                                   return ("Ocurrió un error al crear la colilla")
                           else:
                               print("Fecha hasta no es menor que 10/01/2025")
                               if suba_anual == True:
                                   try:
                                       with conexion.cursor() as cursor:
                                           consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                           cursor.execute(consulta, (
                                               poliza[10], poliza[9], hasta_fecha, self.fecha_actual, self.hora_actual,
                                               usuario_encargado,
                                               poliza[2], poliza[1], int(socio), False))
                                       conexion.commit()
                                       print("Colilla creada")
    
                                       try:
                                           with conexion.cursor() as cursor:
                                               cursor.execute(
                                                   """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                               ultimo_dato_insertado = cursor.fetchone()
                                               print(ultimo_dato_insertado)
                                           try:
                                               valor_total = int(poliza[10]) * int(numero_meses)
                                               with conexion.cursor() as cursor:
                                                   consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                   cursor.execute(consulta, (
                                                   socio, valor_total, self.fecha_actual, ultimo_dato_insertado[6],
                                                   ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                                   ultimo_dato_insertado[9] + ((valor_total) / 2),
                                                   ultimo_dato_insertado[10] + (valor_total / 2),
                                                   ultimo_dato_insertado[11] + valor_total, False, ''))
                                               conexion.commit()
                                               print("Saldo cambiado")
    
                                               try:
                                                   with conexion.cursor() as cursor:
                                                       consulta = "UPDATE polizas SET fecha_desde = %s, fecha_hasta = %s, usuario_ultimo_pago = %s, fecha_ultimo_pago = %s WHERE socio = %s"
                                                       cursor.execute(consulta,
                                                                      (poliza[9], hasta_fecha, usuario_encargado,
                                                                       self.fecha_actual, socio))
                                                   conexion.commit()
    
    
                                                   pdf_colilla(self.fecha_actual, socio, valor_total, poliza[9], hasta_fecha,
                                                               usuario_encargado, poliza[1][0], poliza[2][0])
    
                                                   print("Todos los datos de la colilla se han cambiado correctamente")
                                                   return "Todos los datos de la colilla se han cambiado correctamente"
                                               except psycopg2.Error as e:
    
                                                   return "Ocurrió un error al editar: " + str(e)
                                           except psycopg2.Error as e:
                                               return ("Ocurrió un error al crear el ultimo saldo:" + str(e))
                                       except psycopg2.Error as e:
                                           return ("Ocurrió un error al seleccionar el ultimo:" + str(e))
                                   except psycopg2.Error as e:
                                       return ("Ocurrió un error al crear la colilla")
                               else:
                                   
                                   valor_mes_antiguo = int(poliza[10])
                                   valor_mes_nuevo = int(poliza[10]) + (int(len(poliza[1]))*500)
                                   numero_dia = hasta_fecha_dat.day
                                   numero_mes = hasta_fecha_dat.month
                                   numero_anio = hasta_fecha_dat.year
    
                                   # Fecha de referencia para el cambio de precio
                                   fecha_cambio_precio = datetime(2024, 12, 10).date()  # Convertimos a date
    
                                   valor_total = 0
    
                                   # Recorremos cada mes para determinar el costo
                                   for mes in range(int(numero_meses)):
                                       # Calcula la fecha actual sumando meses (como datetime.date)
                                       fecha_actual = poliza [9] + relativedelta(months=mes)
    
                                       if fecha_actual <= fecha_cambio_precio:
                                           valor_total += valor_mes_antiguo
                                       else:
                                           valor_total += valor_mes_nuevo
    
                                   print(f"El valor total a pagar es: {valor_total}")
                                   
                                   try:
                                       with conexion.cursor() as cursor:
                                           consulta = "INSERT INTO colillas(valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                           cursor.execute(consulta, (
                                               valor_mes_nuevo, poliza[9], hasta_fecha, self.fecha_actual, self.hora_actual,
                                               usuario_encargado,
                                               poliza[2], poliza[1], int(socio), False))
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
                                                   consulta = "INSERT INTO saldo(socio, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, gasto) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                   cursor.execute(consulta, (
                                                   socio, valor_total, self.fecha_actual, ultimo_dato_insertado[6],
                                                   ultimo_dato_insertado[7], ultimo_dato_insertado[8],
                                                   ultimo_dato_insertado[9] + ((valor_total) / 2),
                                                   ultimo_dato_insertado[10] + (valor_total / 2),
                                                   ultimo_dato_insertado[11] + valor_total, False, ''))
                                               conexion.commit()
                                               print("Saldo cambiado")
    
                                               try:
                                                   with conexion.cursor() as cursor:
                                                       consulta = "UPDATE polizas SET fecha_desde = %s, fecha_hasta = %s, usuario_ultimo_pago = %s, fecha_ultimo_pago = %s, suba_anual = %s, valor_mes = %s WHERE socio = %s"
                                                       cursor.execute(consulta,
                                                                      (poliza[9], hasta_fecha, usuario_encargado,
                                                                       self.fecha_actual, True,valor_mes_nuevo,socio))
                                                   conexion.commit()
    
    
                                                   pdf_colilla(self.fecha_actual, socio, valor_total, poliza[9], hasta_fecha,
                                                               usuario_encargado, poliza[1][0], poliza[2][0])
    
                                                   print("Todos los datos de la colilla se han cambiado correctamente")
                                                   return "Todos los datos de la colilla se han cambiado correctamente"
                                               except psycopg2.Error as e:
    
                                                   return "Ocurrió un error al editar: " + str(e)
                                           except psycopg2.Error as e:
                                               return ("Ocurrió un error al crear el ultimo saldo:" + str(e))
                                       except psycopg2.Error as e:
                                           return ("Ocurrió un error al seleccionar el ultimo:" + str(e))
                                   except psycopg2.Error as e:
                                       return ("Ocurrió un error al crear la colilla")
                       else:
                           return ("Excede en la fecha limite 10/01/2026")      
                               
                   else:
                       return ("El cliente no existe")
           except psycopg2.Error as e:
               return "Ocurrio un error al consultar: "+str(e)
       else:
           return "El socio y número de meses deben ser unicamente números"




    def consultar_pagos_documento(self, documento):
        print(documento)
        if documento.isdigit():
            try:
                with conexion.cursor() as cursor:
                    consulta = """
                        SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago, documentos, nombres
                        FROM colillas
                        WHERE %s = ANY (documentos)
                        ORDER BY numero_colilla DESC
                    """
                    cursor.execute(consulta, (int(documento),))
                    colillas = cursor.fetchall()
                    if colillas:
                        # Obtener todos los socios únicos en los resultados
                        socios_encontrados = {colilla[0] for colilla in colillas}  # `colilla[0]` es el campo `socio`
                        
                        if len(socios_encontrados) == 1:
                            # Si todos los registros pertenecen al mismo socio
                            print(colillas)  # Imprime los registros encontrados
                            return colillas
                        else:
                            # Si hay más de un socio en los registros
                            socios_texto = ', '.join(map(str, socios_encontrados))
                            mensaje = f"Se encontraron las pólizas en estos socios: {socios_texto}"
                            print(mensaje)
                            return mensaje
                    else:
                        print("No se encontraron registros asociados al documento")
                        return "No se encontraron registros asociados al documento"
            except psycopg2.Error as e:
                print("Ocurrió un error al consultar: " + str(e))
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "El documento debe ser un número"









    def consultar_colilla_documento(self, documento):
        print(documento)
        if documento.isdigit():
            try:
                with conexion.cursor() as cursor:
                    consulta = """
                        SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago, documentos, nombres 
                        FROM colillas 
                        WHERE %s = ANY (documentos) 
                        ORDER BY socio, numero_colilla DESC
                    """
                    cursor.execute(consulta, (int(documento),))
                    colillas = cursor.fetchall()
                    if colillas:
                        # Dividir los datos por socio y seleccionar el último dato insertado de cada grupo
                        ultimo_colilla_por_grupo = {}
                        for colilla in colillas:
                            socio = colilla[0]
                            if socio not in ultimo_colilla_por_grupo:
                                ultimo_colilla_por_grupo[socio] = colilla
                        # Convertir el diccionario en una lista de valores
                        colillas_finales = list(ultimo_colilla_por_grupo.values())

                        print(colillas_finales)
                        return colillas_finales
                    else:
                        print("No te encuentras en ninguna colilla")
                        return 'No se encontró en ninguna colilla'
            except psycopg2.Error as e:
                print("Ocurrió un error al consultar: " + str(e))
                return "Ocurrió un error al consultar: " + str(e)
        else:
            print(documento)
            return "El documento debe ser un número"

    def leer_colillas_dias (self, numero_dias):
        fecha_actual = datetime.now().date()
        fecha_minima = fecha_actual - timedelta(days=int(numero_dias))
        try:
            print('entre a la consulta')
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM colillas WHERE fecha_pago >= %s ORDER BY fecha_pago DESC;"
                cursor.execute(consulta, (fecha_minima,))
                colillas = cursor.fetchall()
            print(colillas)
            return colillas
        except psycopg2.Error as e:
            return "Ocurrió un error al consultar"

    def consultar_ultimo_pago(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago, documentos, nombres FROM colillas WHERE socio=%s ORDER BY numero_colilla DESC LIMIT 1",
                        (socio,))
                    ultima_colilla = cursor.fetchone()
                    if ultima_colilla:
                        print(ultima_colilla)
                        return ultima_colilla
                    else:
                        print("La póliza no existe")
                        return 'No se encontró ninguna póliza'
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "No es un número de socio correcto"
        
        
        
    def consultar_pagos_socio(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago, documentos, nombres
                        FROM colillas 
                        WHERE socio = %s
                        ORDER BY numero_colilla DESC
                        """,
                        (socio,))
                    pagos = cursor.fetchall()
                    if pagos:
                        print(pagos)  # Imprime todos los registros encontrados
                        return pagos
                    else:
                        print("No se encontraron pagos para el socio")
                        return 'No se encontró ningún pago para el socio'
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "No es un número de socio correcto"



    def eliminar_ultimo_pago(self, socio):
        if socio.isdigit():
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago FROM colillas WHERE socio=%s ORDER BY numero_colilla DESC LIMIT 1",
                        (socio,))
                    ultima_colilla = cursor.fetchone()
                    if ultima_colilla:
                        print(ultima_colilla)

                        try:
                            with conexion.cursor() as cursor:
                                cursor.execute(
                                    "SELECT socio, valor_mes, desde_fecha, hasta_fecha, usuario, fecha_pago, nombres, documentos FROM colillas WHERE socio=%s ORDER BY numero_colilla DESC LIMIT 1 OFFSET 1",
                                    (socio,))
                                penultima_colilla = cursor.fetchone()
                                if penultima_colilla:
                                    print(penultima_colilla)
                                    numero_meses = relativedelta(ultima_colilla[3], ultima_colilla[2]).months + relativedelta(ultima_colilla[3], ultima_colilla[2]).years * 12
                                    valor_restar = ultima_colilla[1]*numero_meses
                                    print(numero_meses, valor_restar)



                                    try:
                                        with conexion.cursor() as cursor:
                                            actualizacion = "UPDATE polizas SET fecha_desde=%s, fecha_hasta=%s, usuario_ultimo_pago=%s, fecha_ultimo_pago=%s WHERE socio=%s"
                                            cursor.execute(actualizacion, (penultima_colilla[2] ,penultima_colilla[3], penultima_colilla[4],penultima_colilla[5],int(socio)))
                                            conexion.commit()
                                        print("Se actualizo la poliza")
                                        fecha_actual = datetime.now().date()
                                        textGas = f"Error creación de colilla {socio}"
                                        try:
                                            with conexion.cursor() as cursor:
                                                consulta = "INSERT INTO gastos(gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado, liquidado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                cursor.execute(consulta, (
                                                str(textGas), valor_restar, ultima_colilla[4], fecha_actual, False, False, True,
                                                False, False))
                                                conexion.commit()
                                            print("Gasto asentado")
                                            try:
                                                with conexion.cursor() as cursor:
                                                    cursor.execute(
                                                        """SELECT * FROM saldo WHERE id_saldo = (SELECT MAX(id_saldo) FROM saldo)""")
                                                    ultimo_dato_insertado = cursor.fetchone()
                                                    print(ultimo_dato_insertado)
                                                try:
                                                    saldo_jefe1 = ultimo_dato_insertado[9] - (int(valor_restar) / 2)

                                                    saldo_jefe2 = ultimo_dato_insertado[10] - (int(valor_restar) / 2)

                                                    with conexion.cursor() as cursor:
                                                        consulta = "INSERT INTO saldo(gasto, valor, fecha, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado, socio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                                                        cursor.execute(consulta, (
                                                        textGas, int(valor_restar), fecha_actual, ultimo_dato_insertado[-7],
                                                        ultimo_dato_insertado[-6],
                                                        int(valor_restar) + int(ultimo_dato_insertado[-5]), saldo_jefe1,
                                                        saldo_jefe2, int(ultimo_dato_insertado[-2]) - int(valor_restar), False,
                                                        0))
                                                        conexion.commit()
                                                    print("Saldo cambiado")





                                                    try:
                                                        with conexion.cursor() as cursor:
                                                            cursor.execute(
                                                                "DELETE FROM colillas WHERE numero_colilla = (SELECT numero_colilla FROM colillas WHERE socio=%s ORDER BY numero_colilla DESC LIMIT 1)",
                                                                (socio,))
                                                            conexion.commit()  # Asegúrate de hacer commit para que los cambios se apliquen
                                                            print("Último pago eliminado exitosamente.")


                                                            pdf_colilla(penultima_colilla[5],socio,int(penultima_colilla[1]),penultima_colilla[2] ,penultima_colilla[3], penultima_colilla[4],str(penultima_colilla[6][0]), str(penultima_colilla[7][0]))
                                                            return ("Último pago eliminado exitosamente.")
                                                    except psycopg2.Error as e:
                                                        return "Ocurrió un error al eliminar el registro: " + str(e)






                                                except psycopg2.Error as e:
                                                    return ("Ocurrió un error al crear el ultimo saldo:", e)
                                            except psycopg2.Error as e:
                                                return ("Ocurrió un error al seleccionar el ultimo:", e)
                                        except psycopg2.Error as e:
                                            return ("Ocurrió un error al asentar el gasto:", e)








                                    except psycopg2.Error as e:
                                        print("Ocurrió un error al modificar la póliza: " + str(e))
                                        return "Ocurrió un error al modificar la póliza: " + str(e)



                                else:
                                    return 'No se encontró un penúltimo pago'
                        except psycopg2.Error as e:
                            return "Ocurrió un error al consultar: " + str(e)

                    else:
                        print("La póliza no existe")
                        return 'No se encontró un último pago'
            except psycopg2.Error as e:
                return "Ocurrió un error al consultar: " + str(e)
        else:
            return "No es un número de socio correcto"