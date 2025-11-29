import networkx as nx
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class Grafo:
    """Clase para manejar grafos dirigidos o no dirigidos."""

    def __init__(self, dirigido=False):
        self.ady = {}
        self.dirigido = dirigido

    # ---------------------------------------------------------
    # MANEJO DE NODOS Y ARISTAS
    # ---------------------------------------------------------
    def agregar_nodo(self, nodo):
        """Agrega un nodo si no existe."""
        if nodo not in self.ady:
            self.ady[nodo] = []
            print(f"Nodo '{nodo}' agregado.")
        else:
            print(f"El nodo '{nodo}' ya existe.")
            

    def agregar_arista(self, origen, destino):
        """Agrega una arista validando que los nodos existan."""
        if origen not in self.ady:
            print(f"El nodo origen '{origen}' no existe.")
            return
        if destino not in self.ady:
            print(f"El nodo destino '{destino}' no existe.")
            return

        self.ady[origen].append(destino)
        if not self.dirigido:
            self.ady[destino].append(origen)

        print(f"Arista '{origen} -> {destino}' agregada.")

    # ---------------------------------------------------------
    # VISUALIZACIÓN
    # ---------------------------------------------------------
    def visualizar(self, titulo="Grafo"):
        """Dibuja el grafo utilizando networkx."""
        G = nx.DiGraph() if self.dirigido else nx.Graph()

        # Agregar nodos
        for nodo in self.ady:
            G.add_node(nodo)

        # Agregar aristas
        for u in self.ady:
            for v in self.ady[u]:
                G.add_edge(u, v)
        #Mostrar gráfico
        plt.figure(figsize=(6, 4))
        plt.title(titulo)

        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_size=800, font_size=12)

        plt.show()
        plt.close()

    # ---------------------------------------------------------
    # MOSTRAR LISTA DE ADYACENCIA
    # ---------------------------------------------------------
    def mostrar_adyacencias(self):
        """Imprime la lista de adyacencia del grafo."""
        print("\n=== Lista de Adyacencia ===")
        for nodo, vecinos in self.ady.items():
            print(f"{nodo} -> {vecinos}")
        print("------------------\n")


# -------------------------------------------------------------
# FUNCIONES DE UTILIDAD (UI)
# -------------------------------------------------------------
def pedir_texto(msg):
    """Solicita texto evitando entradas vacías."""
    valor = input(msg).strip()
    while not valor:
        print("La entrada no puede estar vacía.")
        valor = input(msg).strip()
    return valor


def menu():
    print("¿Deseas un grafo dirigido?")
    opc = input("(s/n): ").strip().lower()
    dirigido = (opc == "s")

    g = Grafo(dirigido=dirigido)

    while True:
        print("\n========= MENÚ =========")
        print("1. Agregar nodo")
        print("2. Agregar arista")
        print("3. Mostrar lista de adyacencia")
        print("4. Visualizar grafo")
        print("5. Salir")
        print("========================")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nodo = pedir_texto("Nombre del nodo: ")
            g.agregar_nodo(nodo)

        elif opcion == "2":
            origen = pedir_texto("Nodo origen: ")
            destino = pedir_texto("Nodo destino: ")
            g.agregar_arista(origen, destino)

        elif opcion == "3":
            g.mostrar_adyacencias()

        elif opcion == "4":
            g.visualizar("Visualización del Grafo")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intenta nuevamente.")


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
if __name__ == "__main__":
    menu()
