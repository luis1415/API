class MySQLConfig:
    HOST = "3.130.126.210"
    USER = "pruebas"
    PASSWORD = "VGbt3Day5R"
    SCHEMA = "habi_db"
    PORT = 3309
    SQL_COMMANDS = {
        "all_properties":
        "SELECT address, city, name, price, description  FROM property as p LEFT JOIN status_history as sh on p.id = sh.id LEFT JOIN status as s on s.id = sh.id WHERE s.name IN ('pre_venta', 'en_venta', 'vendido');",
        "properties_filtered":
        "SELECT address, city, name, price, description  FROM property as p LEFT JOIN status_history as sh on p.id = sh.id LEFT JOIN status as s on s.id = sh.id WHERE s.name IN ('pre_venta', 'en_venta', 'vendido') AND (city = '{0}' OR year = {1} OR name = '{2}') ;",
        "filtered_by_price":
        "SELECT address, city, name, price, description  FROM property as p LEFT JOIN status_history as sh on p.id = sh.id LEFT JOIN status as s on s.id = sh.id WHERE s.name IN ('pre_venta', 'en_venta', 'vendido') AND p.price BETWEEN {0} AND {1} ;",
        "unittest": "SELECT * FROM property LIMIT 1;"
    }
