from BD.Conexion import *
from datetime import datetime, date

# Conexión a la base de datos (simplificado)
basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion = basedatos.conectar()

try:
    socio = str(5002)
    with conexion.cursor() as cursor:
        cursor.execute("SELECT fechas_nacimiento FROM polizas WHERE socio=%s", (socio,))
        poliza = cursor.fetchone()

    if poliza and poliza[0] is not None:
        fechas_nac = poliza[0]

        # Crear lista de fechas de afiliación (ejemplo con fecha base 2090-01-01)
        fechas_afiliacion = [datetime(2060, 1, 1).date() for _ in range(len(fechas_nac))]
        print(fechas_afiliacion)

        mayor_70 = []

        for fecha_nacimiento, fecha_afiliacion in zip(fechas_nac, fechas_afiliacion):
            if isinstance(fecha_nacimiento, datetime):
                fecha_nacimiento = fecha_nacimiento.date()

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
                consulta = "UPDATE polizas SET mayor_70 = %s, fecha_afiliacion = %s WHERE socio = %s"
                cursor.execute(consulta,(mayor_70,fechas_afiliacion, socio))
            conexion.commit()
            print("Todos los datos de la colilla se han cambiado correctamente")

        except psycopg2.Error as e:
            print("Ocurrió un error al editar: " + str(e))


    else:
        print('No se encuentra ninguna poliza')
except psycopg2.Error as e:
    print("Ocurrió un error al consultar:", e)
finally:
    if conexion:
        conexion.close()

