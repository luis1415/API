from services.mysqlbase import MySQLBase


def get_properties(filter, command):
    """Funcion para ejecutar las consultas sql de las propiedades

        Args:
            filter (tuple): es una tupla con los filtros de city, year and status
            command (str): la constante SQL_COMMANDS es un diccionario con las consultas sql,
                           command es la llave del diccionario para acceder a la consulta.
        Return:
            results (dict): diccionario con los resultados de la consulta SQL.
    """
    mysql_processor = MySQLBase()
    results = mysql_processor.execute_command(filter, command)
    return results
