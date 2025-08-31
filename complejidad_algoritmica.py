import time
import random

# -----------------------------
# EJEMPLO DE COMPLEJIDAD
# -----------------------------

# Creamos una lista grande de números ordenados
lista = list(range(1, 1_000_000_000))

# Número objetivo
objetivo = random.choice(lista)

# -----------------------------
# BÚSQUEDA LINEAL - O(n) 
# -----------------------------
def busqueda_lineal(lista, objetivo):
    """Busca el número recorriendo todos los elementos."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve la posición
    return -1  # Si no lo encuentra devolvemos -1

# -----------------------------
# BÚSQUEDA BINARIA - O(log n)
# -----------------------------
def busqueda_binaria(lista, objetivo):
    """Busca el número dividiendo la lista a la mitad en cada paso."""
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# -----------------------------
# COMPARACIÓN DE TIEMPOS
# -----------------------------
inicio = time.time()
busqueda_lineal(lista, objetivo)
fin = time.time()
print(f"El algoritmo de búsqueda lineal tardó: {fin - inicio:.10f} segundos")

inicio = time.time()
busqueda_binaria(lista, objetivo)
fin = time.time()
print(f"El algoritmo de búsqueda binaria tardó: {fin - inicio:.10f} segundos")
