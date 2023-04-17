import mysql.connector
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a la base de datos

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')

# Acceder a las variables de entorno
config = {
    "user": user,
    "password": password,
    "host": host,
    "database": database
}

def new_connection():
    return mysql.connector.connect(**config)