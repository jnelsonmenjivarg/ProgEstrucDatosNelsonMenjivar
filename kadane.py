# Subsequencia contigua con la suma máxima dentro de un arreglo de números (problema del maximum subarray).

import time

def max_subarray_fuerzabruta(arr):
    n = len(arr)
    max_suma = arr[0]
    inicio= fin = 0

    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += arr[j]
            if suma > max_suma:
                max_suma = suma
                inicio, fin = i, j
    return max_suma, arr[inicio:fin+1]


def kadane(arr):
    max_actual = max_global = arr[0]

    for x in arr[1:]:
        max_actual = max(x, max_actual + x)
        if max_actual > max_global:
            max_global = max_actual

    return max_global, arr[1:]

# Ejemplo de aplicacion fuerza bruta subarray
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4,5,6,7,8,9,10]
inicio = time.time()
max_subarray_fuerzabruta(nums)
fim = time.time()
print("Fuerza bruta maximo subarray:",  round(fim - inicio, 12), "Segundos")


# Ejemplo de usoaplicacion de kadane
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4,5,6,7,8,9,10]
inicio = time.time()
kadane(nums)
fim = time.time()
print("Kadane maximo subarray:",  round(fim - inicio, 12), "Segundos")
print("Tarea de Nelson Menjivar")