import time

# Algoritmo de fuerza bruta (iterativo)

def sumcuadrad_fuerzbruta(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total

# Algoritmo óptimo (fórmula)
# Suma de los primeros n cuadrados: n(n+1)(2n+1)/6

def sumcuadrad_optima(n):
    return (n * (n + 1) * (2*n + 1)) // 6

# Medir tiempo de ejecución, se tomara un millon como tamaño de prueba
n = 1_000_000_000  # tamaño de prueba, mil millones

print(f"-------Prueba------- con {n} elementos")
# Fuerza bruta
tincio = time.time()
resultado_fb = sumcuadrad_fuerzbruta(n)
tfin = time.time()
print(f"Fuerza bruta: con {n}  {resultado_fb}, Tiempo: {tfin - tincio:.6f} segundos")

# AInvocacion a la funcion del allgoritmo óptimo
tincio = time.time()
result_optima = sumcuadrad_optima(n)
tfin = time.time()
print(f"Óptimo: con {n} {result_optima}, Tiempo: {tfin - tincio:.5f} segundos")
