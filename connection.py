import mysql.connector
# Configuración de la conexión a la base de datos
config = {
    "user": "hrp",
    "password": "1234",
    "host": "localhost",
    "database": "mi_base_datos"
}

def new_connection():
    return mysql.connector.connect(**config)