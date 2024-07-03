
import psycopg2
import subprocess
import os
from datetime import datetime
import io
class Database():
    user = ""
    password =""
    host =""
    def __init__(self, user, password, host):
         self.user =user
         self.password =password
         self.host = host
         print(self.user)
         print(self.password)
         print(self.host)

    def conectar(self):
         try:
             credenciales = {
                 "dbname" : "funeraria" ,
                 "user" : self.user ,
                 "password" : self.password ,
                 "host" : self.host ,
                 "port" : 5432
             }
             print(credenciales)
             conexion= psycopg2.connect(**credenciales)
             print(conexion)
             if conexion:
                 print("conexion exitosa")
                 self.conexion = conexion
             return conexion
         except psycopg2.Error as e:
             print("Ocurrio un error al conectar a PostgreSQL")

    import os
    import io

    import os
    import subprocess

    def crear_copia_seguridad(self):
        print('Entré en la función de copia de seguridad')
        db_name = "funeraria"
        # Definir la ruta completa del archivo de copia de seguridad
        ruta_completa = r'C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\copia_bases'
        archivo = os.path.join(ruta_completa, 'copia.sql')

        # Crear el directorio si no existe
        os.makedirs(ruta_completa, exist_ok=True)

        # Configurar el comando pg_dump
        comando = [
            'pg_dump',
            '--dbname=postgresql://{}:{}@{}:{}/{}'.format(self.user, self.password,  self.host, 5432, db_name),
            '--file', archivo
        ]

        try:
            # Ejecutar el comando pg_dump
            result = subprocess.run(comando, check=True, text=True, capture_output=True)
            print(f'Copia de seguridad creada exitosamente en {archivo}')

        except subprocess.CalledProcessError as e:
            print(f'Ocurrió un error al crear la copia de seguridad: {e.stderr}')




