def busqueda_exhaustiva(posicion_inicial, posicion_objetivo, max_busqueda=10):
    # Movimientos posibles: izquierda (-1) y derecha (+1)
    movimientos = [-1, 1]
    pasos = 0

    while pasos <= max_busqueda:
        for movimiento in movimientos:
            nueva_posicion = posicion_inicial + (pasos * movimiento)
            print(f"Explorando posición: {nueva_posicion}")
            if nueva_posicion == posicion_objetivo:
                print(f"Posición encontrada en {pasos} pasos.")
                return nueva_posicion
        pasos += 1

    print("No se encontró la posición en el rango de búsqueda que elegiste.")
    return None

# Consola para que se ingresen los datos
posicion_inicial = int(input("Ingrese la posición inicial del bloque: "))
posicion_objetivo = int(input("Ingrese la posición objetivo de montaje: "))

# Se ejecuta la busqueda exhaustiva
busqueda_exhaustiva(posicion_inicial, posicion_objetivo)

