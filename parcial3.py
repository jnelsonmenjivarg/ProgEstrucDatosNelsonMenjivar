# Manejo de  canciones por genero y Artista
# Descripción: Parcial III

class Nodo:
    def __init__(self, tipo, nombre):
        # "genero" o "artista"
        self.tipo = tipo  
        self.nombre = nombre
        # Arreglo de lista de subnodos para artistas o canciones)
        self.arts_cancs = []  

    #Adiciona un artista o cancion al nodo
    def agregar_artcan(self, artcan):
        self.arts_cancs.append(artcan)

    # Pone en mayuscula la primera letra del tipo y muestra el nombre
    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.nombre}"

#Clase Cancion, asignacion de nombre y letra
class Cancion:
    def __init__(self, nombre, letra):
        self.nombre = nombre
        self.letra = letra

    #Metodo para mostrar el nombre de la cancion
    def __str__(self):
        return f"cancion: {self.nombre}"


# Estas son la funciones principales del recorridos de los nodos del árbol
def iterar_arbol(nodo, nivel=0):
    print("  " * nivel + str(nodo))
    if hasattr(nodo, "arts_cancs"):
        for artcan in nodo.arts_cancs:
            iterar_arbol(artcan, nivel + 1)

#Metodo para buscar genero por nombre.
def buscar_genero(raiz, nombre):
    for genero in raiz:
        if genero.nombre.lower() == nombre.lower():
            return genero
    return None


#Busca un artista en todos los generos definidos
def buscar_artista(raiz, nombre_artista):
   #Doble lazo iteractivo para recorrer generos y artistas
   #Por cada genero busca el artista.
    for genero in raiz:
        for artista in genero.arts_cancs:
            if artista.nombre.lower() == nombre_artista.lower():
                return artista
    return None

#Busca una cancion en todo el árbol definido.
def buscar_cancion(raiz, nombre_cancion):
    #La escencia esta aqui, triple lazo para recorrer generos, artistas y canciones
    
    #Lazo para for genero que es la raiz:
    for genero in raiz:
        #Lazo para cada artista en el genero
        for artista in genero.arts_cancs:
            #Lazo para cada cancion en el artista
            for cancion in artista.arts_cancs:
                #Se hacen minusculas ambbos para que la comparacion sea en las mismas condiciones
                if cancion.nombre.lower() == nombre_cancion.lower():
                    return cancion
    return None

#Metodo para crear un nuevo elemento en el árbol ya sea genero, artista o cancion.
def crear_elemento(raiz):
    #Se solicita el tipo de elemento a crear
    tipo = input("Ingrese el tipo de elemento (Genero=G, Artista= A o Cancion = C): ").strip().lower()[0:1]

    if tipo == "g":
        nombre = input("Nombre del genero: ")
        raiz.append(Nodo("genero", nombre))
        print(f"Genero '{nombre}' agregado con éxito.")

    elif tipo == "a":
        nombre_genero = input("Ingrese el genero al que pertenece el artista: ")
        genero = buscar_genero(raiz, nombre_genero)
        if genero:
            nombre_artista = input("Nombre del artista: ")
            genero.agregar_artcan(Nodo("artista", nombre_artista))
            print(f"Cantante o medio Artista '{nombre_artista}' agregado al genero '{nombre_genero}'.")
        else:
            print("enero no encontrado.")

    elif tipo == "c":
        nombre_artista = input("Ingrese el artista al que pertenece la cancion: ")
        artista = buscar_artista(raiz, nombre_artista)
        if artista:
            # Buscar el género al que pertenece este artista
            nombre_genero = None
            for genero in raiz:
                if artista in genero.arts_cancs:
                    nombre_genero = genero.nombre
                    break

            nombre_cancion = input("Nombre de la cancion: ")
            letra = input("Ingrese la letra de la cancion: ")
            artista.agregar_artcan(Cancion(nombre_cancion, letra))

            # Si se encontró el género, se muestra correctamente, si no, se indica desconocido
            if nombre_genero:
                print(f"Cancion '{nombre_cancion}' agregada al artista '{nombre_artista}' en el genero '{nombre_genero}'.")
            else:
                print(f"ancion '{nombre_cancion}' agregada al artista '{nombre_artista}'. (Género no encontrado)")
        else:
            print("Cantante no encontrado.")
    else:
        print("Tipo de cancion no encontrado...!!!")


def mostrar_canciones_por_genero(raiz):
    nombre_genero = input("Ingrese el nombre del genero: ")
    genero = buscar_genero(raiz, nombre_genero)
    if genero:
        print(f"Canciones del genero '{nombre_genero}':")
        for artista in genero.arts_cancs:
            for cancion in artista.arts_cancs:
                print(f"  - Canción: '{cancion.nombre}' del Artista: '{artista.nombre}'")
    else:
        print("Genero no encontrado.")


def mostrar_canciones_por_artista(raiz):
    nombre_artista = input("Ingrese el nombre del artista: ")
    artista = buscar_artista(raiz, nombre_artista)
    if artista:
        print(f"Canciones del artista '{nombre_artista}':")
        for cancion in artista.arts_cancs:
            print(f"  - Canción: '{cancion.nombre}'")
    else:
        print("Artista no encontrado.")


def mostrar_letra(raiz):
    nombre_cancion = input("Ingrese el nombre de la cancion: ")
    cancion = buscar_cancion(raiz, nombre_cancion)
    if cancion:
        print(f"Letra de Canción '{cancion.nombre}' Letra: \n{cancion.letra}")
    else:
        print("Cancion no encontrada.")


def editar_letra(raiz):
    nombre_cancion = input("Ingrese el nombre de la cancion a editar: ")
    cancion = buscar_cancion(raiz, nombre_cancion)
    if cancion:
        print(f"Leyenda actual:\n{cancion.letra}")
        nueva_letra = input("Ingrese la nueva letra: ")
        cancion.letra = nueva_letra
        print(f"Letra de '{cancion.nombre}' actualizada con éxito.")
    else:
        print("Cancion no encontrada.")


# Menu para la ejecucion

def menu():
    raiz = []  # Lista de generos (nivel superior)

    while True:
        print("\n===<<< MENÚ PRINCIPAL >>>===")
        print("1. Recorrer árbol completo")
        print("2. Crear elemento (Genero=G, Artista= A o Cancion = C)")
        print("3. Buscar y mostrar canciones de un genero")
        print("4. Buscar y mostrar canciones de un artista")
        print("5. Buscar y mostrar letra de una cancion")
        print("6. Editar letra de una cancion")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if raiz:
                for genero in raiz:  iterar_arbol(genero)
            else:  print("No hay generos creados aún.")

        elif opcion == "2": crear_elemento(raiz)

        elif opcion == "3": mostrar_canciones_por_genero(raiz)

        elif opcion == "4": mostrar_canciones_por_artista(raiz)

        elif opcion == "5": mostrar_letra(raiz)

        elif opcion == "6": editar_letra(raiz)

        elif opcion == "7":
            print("Abandonando el sistema...")
            break
        else:
            print("Opción Invalida. Intente mas tarde.")


if __name__ == "__main__":
    menu()
