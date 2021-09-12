import pymysql
from services.mysqlconfig import MySQLConfig


class MySQLBase(object):
    def __init__(self):
        self.error = ""
        self.status = 0

    def connect(self,
                host=MySQLConfig.HOST,
                user=MySQLConfig.USER,
                password=MySQLConfig.PASSWORD,
                schema=MySQLConfig.SCHEMA,
                port=MySQLConfig.PORT):
        """Funcion para conectar con MySQL 

        Args:
            host (str): el host de mysql
            user (str): el usuario de mysql
            password (str): el password de mysql
            schema (str): el schema de mysql
            port (int): el puerto de mysql
        
        Return:
            db_connection (object): objeto de conexion con mysql

        """
        try:
            db_connection = pymysql.connect(host=host,
                                            port=port,
                                            user=user,
                                            passwd=password,
                                            db=schema,
                                            charset="utf8",
                                            init_command="set names utf8")

            self.status = 1

            return db_connection
        except Exception as e:
            self.error = f"Error: {e}"
            self.status = 0

    def execute_command(self, command, filter=""):
        """Funcion para ejecutar las consultas sql de las propiedades

        Args:
            filter (tuple): es una tupla con los filtros de city, year and status, por defecto es str vacio
            command (str): la constante SQL_COMMANDS es un diccionario con las consultas sql,
                           command es la llave del diccionario para acceder a la consulta.

        Return:
            results (dict): un diccionario con los resultados de la consulta SQL.
        """
        db_conn = self.connect()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(MySQLConfig.SQL_COMMANDS[command].format(*filter))
        results = cursor.fetchall()
        db_conn.close()
        return results
