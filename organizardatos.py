from BD.Conexion import *
from datetime import datetime, timedelta

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion = basedatos.conectar()

valor_por_defecto = ''

try:
    with conexion.cursor() as cursor:
        # Obtener los datos actuales
        cursor.execute("SELECT socio,nombres,documentos,fechas_nacimiento,parentesco_titular nombres FROM polizas;")
        polizas = cursor.fetchall()
        for poliza in polizas:
            print(poliza)
            socio = poliza[0]
            nombres = poliza[1]
            documentos = poliza[2]
            fechas_nacimiento = poliza[3]
            parentesco_titular = poliza[4]



            max_length = max(len(nombres), len(documentos), len(fechas_nacimiento), len(parentesco_titular))

            nombres = list(nombres) + [valor_por_defecto] * (max_length - len(nombres))
            documentos = list(documentos) + [valor_por_defecto] * (max_length - len(documentos))
            fechas_nacimiento = list(fechas_nacimiento) + [valor_por_defecto] * (max_length - len(fechas_nacimiento))
            parentesco_titular = list(parentesco_titular) + [valor_por_defecto] * (max_length - len(parentesco_titular))


            print(fechas_nacimiento)
            nombres_str = '{{{}}}'.format(
                ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, nombres))))
            parentesco_titular_str = '{{{}}}'.format(
                ','.join(filter(None, map(lambda x: 'NULL' if x == valor_por_defecto else x, parentesco_titular))))

            fechas_nacimiento2 = [datetime(2000, 1, 1) if fecha == valor_por_defecto else fecha for fecha in fechas_nacimiento]


            # Convierte las fechas a objetos datetime

            print(nombres_str)
            print(parentesco_titular_str)
            print(fechas_nacimiento2)
            print(parentesco_titular_str)
            try:
                with conexion.cursor() as cursor:
                    actualizacion = "UPDATE polizas SET documentos=%s, nombres=%s, fechas_nacimiento=%s, parentesco_titular=%s WHERE socio=%s"
                    cursor.execute(actualizacion, (
                        documentos, nombres_str, fechas_nacimiento2, parentesco_titular_str,
                        int(socio)))
                    conexion.commit()
                print("Todo generado con éxito")
            except psycopg2.Error as e:
                print("Ocurrió un error al modificar la póliza: " + str(e))

except psycopg2.Error as e:
    print("Ocurrió un error:", str(e))


