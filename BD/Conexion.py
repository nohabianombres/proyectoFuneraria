import psycopg2

class Database():
    user = "postgres"
    password ="GGLLiDeqFmoTGLXgJbndSxjieiUqNPxK"
    host ="viaduct.proxy.rlwy.net"
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
                 "dbname" : "railway" ,
                 "user" : self.user ,
                 "password" : self.password ,
                 "host" : self.host ,
                 "port" : 38680
             }
             print(credenciales)
             conexion= psycopg2.connect(**credenciales)
             print(conexion)
             if conexion:
                 print("conexion exitosa")
             return conexion
         except psycopg2.Error as e:
             print("Ocurrio un error al conectar a PostgreSQL")
