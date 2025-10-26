# --- 1. Definición del Nodo ---

class Nodo:
    def __init__(self, valor):
        self.valor = valor      # El dato que guardamos
        self.izquierdo = None   # El hijo izquierdo (menor)
        self.derecho = None     # El hijo derecho (mayor)


# --- 2. Definición de la Clase del Árbol ---
class ArbolBinarioBusqueda:
    def __init__(self):
        # El árbol empieza vacío, su raíz es Nula.
        self.raiz = None

    # --- INSERCIÓN ---
    
    def insertar(self, valor):
        """Método público para insertar un valor."""
        # Si el árbol está vacío, el nuevo nodo es la raíz
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            # Si no, llamamos a la función recursiva
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        # Método privado recursivo para encontrar dónde insertar.
        if valor < nodo.valor:
            # Si el valor es menor que el nodo.valor, vamos a la izquierda
            if nodo.izquierdo is None:
                # Si no hay hijo izquierdo, este es su lugar
                nodo.izquierdo = Nodo(valor)
            else:
                # Si hay hijo izquierdo, repetimos el proceso desde allí
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            # El valor es mayor, vamos a la derecha
            if nodo.derecho is None:
                # Si no hay hijo derecho, este es su lugar
                nodo.derecho = Nodo(valor)
            else:
                # Si hay hijo derecho, repetimos el proceso desde allí
                self._insertar(nodo.derecho, valor)
        # else:
            # Si el valor es igual, no hacemos nada (no se permiten duplicados)


    # --- BÚSQUEDA ---
    
    def buscar(self, valor):
        """MétOdo público para buscar un valor."""
        return self._buscarrecursivo(self.raiz, valor)

    def _buscarrecursivo(self, nodo_actual, valor):
        """Método privado recursivo para buscar."""
        # Caso 1: El nodo no existe (llegamos al final)
        if nodo_actual is None:
            return False
        
        # Caso 2: Encontramos el valor
        if nodo_actual.valor == valor:
            return True
        
        # Caso 3: El valor es menor, buscamos a la izquierda
        if valor < nodo_actual.valor:
            return self._buscarrecursivo(nodo_actual.izquierda, valor)
        
        # Caso 4: El valor es mayor, buscamos a la derecha
        return self._buscarrecursivo(nodo_actual.derecha, valor)

    # --- RECORRIDOS (DFS) ---

    # IN-ORDEN (Izquierda, Raíz, Derecha)
    # Útil para obtener los datos ordenados
    def inorden(self):
        print("Recorrido In-orden (ordenado):")
        self._inorden(self.raiz)
        print() # Nueva línea al final

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self._inorden(nodo.derecho)



    # PRE-ORDEN (Raíz, Izquierda, Derecha)
    # Útil para copiar el árbol
    def preorden(self):
        print("Recorrido Pre-orden:")
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=" ")
            self._preorden(nodo_actual.izquierdo)
            self._preorden(nodo_actual.derecho)

    # POST-ORDEN (Izquierda, Derecha, Raíz)
    # Útil para eliminar el árbol de la memoria
    def postorden(self):
        print("Recorrido Post-orden:")
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden(nodo_actual.izquierdo)
            self._postorden(nodo_actual.derecho)
            print(nodo_actual.valor, end=" ")

    # --- ELIMINACIÓN ---
    
    def eliminar(self, valor):
        #Método público para eliminar un nodo.
        self.raiz = self._eliminarrecursivo(self.raiz, valor)

    def _encontrarminimo(self, nodo_actual):
        # Encuentra el nodo con el valor más pequeño en un subárbol.
        # El valor más pequeño siempre está en el hijo más a la izquierda.
        while nodo_actual.izquierdo is not None:
            nodo_actual = nodo_actual.izquierdo
        return nodo_actual

    def _eliminarrecursivo(self, nodo_actual, valor):
        # Caso 0: No encontramos el nodo
        if nodo_actual is None:
            return None

        # Paso 1: Buscar el nodo a eliminar
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo= self._eliminarrecursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminarrecursivo(nodo_actual.derecha, valor)
        else:
            # ¡Encontramos el nodo! Ahora vemos los 3 casos de eliminación.

            # Caso 1: Nodo Hoja (sin hijos)
            if nodo_actual.izquierdo is None and nodo_actual.derecha is None:
                return None # Simplemente lo borramos
            
            # Caso 2: Nodo con un solo hijo (izquierdo o derecho)
            elif nodo_actual.izquierdo is None:
                return nodo_actual.derecha # Su hijo derecho toma su lugar
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierdo# Su hijo izquierdo toma su lugar

            # Caso 3: Nodo con dos hijos
            # Se busca el sucesor (el valor más pequeño de la rama derecha)
            sucesor = self._encontrarminimo(nodo_actual.derecha)
            
            # Copiamos el valor del sucesor al nodo actual
            nodo_actual.valor = sucesor.valor
            
            # Eliminamos el sucesor (que ahora está duplicado) de la rama derecha
            nodo_actual.derecha = self._eliminarrecursivo(nodo_actual.derecha, sucesor.valor)

        return nodo_actual


# --- 3. Ejemplo de Uso ---
if __name__ == "__main__":
    
      #Esta es un forma de insertar los valores.
    # bst.insertar(8)
    # bst.insertar(3)
    # bst.insertar(10)
    # bst.insertar(1)
    # bst.insertar(6)
    # bst.insertar(14)

    #Esta es otra forma de insertar los valores, mas elegante
    # Se  debe crear una instancia del árbol
    bst = ArbolBinarioBusqueda()
    #Se debe hacer un array con la lista de valores
    valores=[50,30,70,20,40,60,80]
    # Se recorre en un lazo lel arrar pra Insertar los valores del ejemplo anterior
    # (8, 3, 10, 1, 6, 14)
    
    for v in valores:
        bst.insertar(v)

  

    # Mostramos los recorridos
    bst.inorden()   # Debería mostrar: 1 3 6 8 10 14
    bst.preorden()  # Debería mostrar: 8 3 1 6 10 14    
    bst.postorden() # Debería mostrar: 1 6 3 14 10 8

