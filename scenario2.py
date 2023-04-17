import os
import threading
import time
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import connection as conn
import mysql_functions as my_f

# Obtener el tiempo actual
tiempo_inicio = time.time()

# Parámetros para la ejecución de los hilos
cantidad_incremento = int(os.getenv("cantidad_incremento"))
cantidad_decremento = int(os.getenv("cantidad_decremento"))
intervalo_incremento = int(os.getenv("intervalo_incremento"))
intervalo_decremento = int(os.getenv("intervalo_decremento"))
tiempo_ejecucion = int(os.getenv("tiempo_ejecucion"))

# Intentar conectar a la base de datos
try:
    mydb = conn.new_connection()
    mydb2 = conn.new_connection()

    my_f.initialize_dba(mydb)

    # Creación de los hilos
    hilo_incrementar = threading.Thread(target=my_f.incrementar_lock, args=(cantidad_incremento, intervalo_incremento, tiempo_ejecucion, mydb))
    hilo_decrementar = threading.Thread(target=my_f.decrementar_lock, args=(cantidad_decremento, intervalo_decremento, tiempo_ejecucion, mydb2))

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
        mydb.close()
    except:
        print("No se pudo cerrar la conexión a la base de datos")

# Obtener el tiempo actual de nuevo
tiempo_fin = time.time()
# Calcular la diferencia
tiempo_ejecucion = tiempo_fin - tiempo_inicio
print("La aplicación ha tardado", tiempo_ejecucion, "segundos en ejecutarse.")