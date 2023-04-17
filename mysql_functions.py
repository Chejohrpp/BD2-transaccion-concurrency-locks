import time

# Función que incrementa la cantidad de la tabla Movimiento
def incrementar(cantidad, intervalo, tiempo_ejecucion,mydb):
    cursor = mydb.cursor()
    tiempo_inicio = time.time()
    tiempo_final = tiempo_inicio + tiempo_ejecucion

    while time.time() < tiempo_final:
        cursor.execute("UPDATE Movimiento SET cantidad = cantidad + %s WHERE id = 1", (cantidad,))
        mydb.commit()
        getCant(cantidad, cursor, "incrementada")
        time.sleep(intervalo)

# Función que decrementa la cantidad de la tabla Movimiento
def decrementar(cantidad, intervalo, tiempo_ejecucion,mydb):
    cursor = mydb.cursor()
    tiempo_inicio = time.time()
    tiempo_final = tiempo_inicio + tiempo_ejecucion

    while time.time() < tiempo_final:
        cursor.execute("UPDATE Movimiento SET cantidad = cantidad - %s WHERE id = 1", (cantidad,))
        mydb.commit()
        getCant(cantidad, cursor, "decrementada")
        time.sleep(intervalo)

# Obtener la cantidad final de la tabla Movimiento
def getCant(cantidad, cursor, funcion):
    cursor.execute("SELECT cantidad FROM Movimiento")
    cantidad_final = cursor.fetchone()[0]
    print(f"Cantidad {funcion} en {cantidad} unidades. Cantidad actual: {cantidad_final}")

# Valor inicial de la tabla Movimiento
def initialize_dba(mydb):
    cursor = mydb.cursor()
    # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM Movimiento")
    result = cursor.fetchone()[0]
    if result == 0:
        cursor.execute("INSERT INTO Movimiento (cantidad) VALUES (0)")
        mydb.commit()

# Función que incrementa la cantidad de la tabla Movimiento
def incrementar_lock(cantidad, intervalo, tiempo_ejecucion, mydb):
    cursor = mydb.cursor()
    tiempo_inicio = time.time()
    tiempo_final = tiempo_inicio + tiempo_ejecucion

    while time.time() < tiempo_final:
        cursor.execute("SELECT cantidad FROM Movimiento WHERE id = 1 FOR UPDATE")
        cantidad_actual = cursor.fetchone()[0]
        cantidad_nueva = cantidad_actual + cantidad
        cursor.execute("UPDATE Movimiento SET cantidad = %s WHERE id = 1", (cantidad_nueva,))
        mydb.commit()
        getCant(cantidad, cursor, "incrementada")
        time.sleep(intervalo)

# Función que decrementa la cantidad de la tabla Movimiento
def decrementar_lock(cantidad, intervalo, tiempo_ejecucion, mydb):
    cursor = mydb.cursor()
    tiempo_inicio = time.time()
    tiempo_final = tiempo_inicio + tiempo_ejecucion

    while time.time() < tiempo_final:
        cursor.execute("SELECT cantidad FROM Movimiento WHERE id = 1 FOR UPDATE")
        cantidad_actual = cursor.fetchone()[0]
        cantidad_nueva = cantidad_actual - cantidad
        cursor.execute("UPDATE Movimiento SET cantidad = %s WHERE id = 1", (cantidad_nueva,))
        mydb.commit()
        getCant(cantidad, cursor, "decrementada")
        time.sleep(intervalo)