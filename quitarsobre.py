from BD.Conexion import *

from BD.Conexion import *

basedatos = Database("postgres", "87b3d9baf", "localhost")
conexion = basedatos.conectar()

try:
    with conexion.cursor() as cursor:
        # Obtener los datos actuales
        cursor.execute("SELECT socio, nombres FROM polizas;")
        nombres_result = cursor.fetchall()
        lista_nombres_sin_n = [(id, [nombre.strip() for nombre in nombres]) for id, nombres in nombres_result]

        # Modificar los datos (quitar '\n') y actualizar la tabla
        for id, nombres in lista_nombres_sin_n:
            nuevos_nombres = [nombre.replace('\n', '') for nombre in nombres]

            # Actualizar la tabla con los nuevos datos
            cursor.execute("UPDATE polizas SET nombres = %s WHERE socio = %s;", (nuevos_nombres, id))

        # Confirmar los cambios en la base de datos
        conexion.commit()

except psycopg2.Error as e:
    print("Ocurrió un error al modificar los datos:", str(e))
finally:
    # No olvides cerrar la conexión
    conexion.close()
