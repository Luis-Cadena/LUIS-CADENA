print("Búsqueda en Arreglo Multidimensional")

matriz_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

valor_buscado = 6

if any(valor_buscado in fila for fila in matriz_1):
    print(f"se encontró {valor_buscado} en la matriz.")

else:
    print(f"{valor_buscado} no se encontró en la matriz")