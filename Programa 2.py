
def burbuja(matriz, fila_a_ordenar):
    # Aplica el algoritmo burbuja a la fila seleccionada
    for i in range(len(matriz[fila_a_ordenar]) - 1):
        for j in range(len(matriz[fila_a_ordenar]) - 1 - i):
            if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
                # Intercambio de elementos
                matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]
    return matriz

# Matriz de ejemplo
matriz = [[21, 34, 56],
          [24, 33, 11],
          [44, 51, 18]]

# Selecciona la fila a ordenar
fila_a_ordenar = 1  # Puedes cambiar este valor para ordenar una fila diferente

# Llamada a la función
matriz_ordenada = burbuja(matriz, fila_a_ordenar)

# Imprime la matriz ordenada
print("Matriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)












