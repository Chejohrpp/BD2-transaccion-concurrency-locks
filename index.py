# Load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

import threading
import mysql.connector
import time

import mysql_functions as my_f
import connection as connect

#escenario 1

# Obtener el tiempo actual
tiempo_inicio = time.time()

# Parámetros para la ejecución de los hilos
cantidad_incremento = int(os.getenv("cantidad_incremento"))
cantidad_decremento = int(os.getenv("cantidad_decremento"))
intervalo_incremento = int(os.getenv("intervalo_incremento"))
intervalo_decremento = int(os.getenv("intervalo_decremento"))
tiempo_ejecucion = int(os.getenv("tiempo_ejecucion"))

try:
    # Intentar conectar a la base de datos
    connection = connect.new_connection()
    connection2 = connect.new_connection()
    my_f.initialize_dba(connection)
    # Creación de los hilos
    hilo_incrementar = threading.Thread(target=my_f.incrementar, args=(cantidad_incremento, intervalo_incremento, tiempo_ejecucion,connection))
    hilo_decrementar = threading.Thread(target=my_f.decrementar, args=(cantidad_decremento, intervalo_decremento, tiempo_ejecucion,connection2))

    # Inicio de los hilos
    hilo_incrementar.start()
    hilo_decrementar.start()

    # Espera a que los hilos terminen
    hilo_incrementar.join()
    hilo_decrementar.join()

except mysql.connector.Error as err:
    print(f"Error de conexión a la base de datos: {err}")
finally:
    # Cerrar la conexión
    try:
        connection.close()
        connection2.close()
    except:
        print(f"NO se cerro la base de datos " )

# Obtener el tiempo actual de nuevo
tiempo_fin = time.time()
# Calcular la diferencia
tiempo_ejecucion = tiempo_fin - tiempo_inicio
print("La aplicación ha tardado", tiempo_ejecucion, "segundos en ejecutarse.")
