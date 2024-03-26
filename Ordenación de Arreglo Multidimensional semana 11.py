print("Ordenación de Arreglo Multidimensional")
matriz_2 = [
    [8, 3, 4],
    [1, 1, 11],
    [0, 12, 1]
]

def buble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        j: int
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def mostrar_matriz(matriz_2):
      for fila in matriz_2:
            print(fila)

print("Matriz Original:")
mostrar_matriz(matriz_2)

for fila in matriz_2:
      buble_sort_fila(fila)

print("\nMatriz ordenadas por filas")
mostrar_matriz(matriz_2)