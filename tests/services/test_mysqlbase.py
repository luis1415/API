import unittest
from services.mysqlbase import MySQLBase


class TestMySQLBase(unittest.TestCase):
    def test_connect(self):
        """Funcion para testear la conexion con mysql, cuando es status = 1 es conexion exitosa.
        """
        db_connect = MySQLBase()
        db_connect.connect()
        self.assertEqual(db_connect.status, 1)
        self.assertEqual(db_connect.error, "")

    def test_execute_command(self):
        """Funcion para testear que se ejecute un comando SQL y devuelva un resultado
        """
        db_connect = MySQLBase()
        result = db_connect.execute_command("", "unittest")
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()