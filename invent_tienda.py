# Simulación de sistema de inventario básico para una tienda

inventario = {
    "leche": 1.50,
    "queso lb": 3.25,
    "huevos": 0.25,
    "harina": 2.25
}

agotados = {"huevos","harina"}  # Conjunto de productos sin stock

def mostrar_inventario():
    print("\n INVENTARIO ACTUAL:")
    for producto, precio in inventario.items():
        estado = " Agotado" if producto in agotados else " Disponible"
        print(f"- {producto.capitalize():<10} | ${precio:.2f} | {estado}")
    print(f"\nTotal de productos: {len(inventario)}\n")

def verificar_disponibilidad():
    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in inventario:
        if producto in agotados:
            print(f" El producto '{producto}' está AGOTADO.")
        else:
            print(f" El producto '{producto}' está disponible (${inventario[producto]:.2f}).")
    else:
        print(f" El producto '{producto}' no existe en el inventario.")

def agregar_producto():
    producto = input(" Nombre del nuevo producto: ").lower()
    if producto in inventario:
        print(f" El producto '{producto}' ya existe.")
        return
    try:
        precio = float(input("Ingrese el precio: "))
        if precio < 0:
            print(" El precio no puede ser negativo.")
            return
    except ValueError:
        print(" Ingrese un valor numérico válido para el precio.")
        return

    inventario[producto] = precio
    print(f" Producto '{producto}' agregado correctamente.")

def eliminar_producto():
    producto = input(" Ingrese el nombre del producto a eliminar: ").lower()
    if producto in inventario:
        del inventario[producto]
        agotados.discard(producto)
        print(f" Producto '{producto}' eliminado correctamente.")
    else:
        print(f"El producto '{producto}' no existe en el inventario.")

def mostrar_agotados():
    if agotados:
        print("\n PRODUCTOS AGOTADOS:")
        for producto in agotados:
            print(f"- {producto.capitalize()}")
    else:
        print("\n No hay productos agotados actualmente.")

def mostrar_disponibles():
    disponibles = {p: v for p, v in inventario.items() if p not in agotados}
    if disponibles:
        print("\nPRODUCTOS DISPONIBLES:")
        for producto, precio in disponibles.items():
            print(f"- {producto.capitalize():<10} | ${precio:.2f}")
            print(f"\nTotal disponibles: {len(disponibles)}")
    else:
        print("\n No hay productos disponibles.")

# --- Menú principal con match-case ---
def menu():
    while True:
        print("""
========= SISTEMA DE INVENTARIO =========
1. Ver inventario
2. Validar disponibilidad de producto
3. Agregar producto
4. Eliminar producto
5. Mostrar productos agotados
6. Mostrar productos disponibles
7. Salir
============================================
""")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                mostrar_inventario()
            case "2":
                verificar_disponibilidad()
            case "3":
                agregar_producto()
            case "4":
                eliminar_producto()
            case "5":
                mostrar_agotados()
            case "6":
                mostrar_disponibles()
            case "7":
                print("Saliendo del sistema... ¡Hasta luego!!!")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    menu()
