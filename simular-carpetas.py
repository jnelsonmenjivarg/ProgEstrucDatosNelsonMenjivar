import tkinter as tk

class Carpeta:
    """Clase que define una carpeta en el sistema de archivos"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcarpetas = {}

    def crear_subcarpeta(self, nombre):
        """Crea una subcarpeta dentro de la carpeta actual"""
        if nombre in self.subcarpetas:
            return f"La carpeta '{nombre}' ya existe."
        else:
            self.subcarpetas[nombre] = Carpeta(nombre)
            return f"Carpeta '{nombre}' creada correctamente."

    def eliminar_subcarpeta(self, nombre):
        """Elimina una subcarpeta existente"""
        if nombre in self.subcarpetas:
            del self.subcarpetas[nombre]
            return f"Carpeta '{nombre}' eliminada correctamente."
        else:
            return f"❌ No existe la carpeta '{nombre}'."

    def ver_contenido(self, nivel=0):
        """Devuelve el árbol de carpetas como texto"""
        estructura = "  " * nivel + f"{self.nombre}\n"
        for subcarpeta in self.subcarpetas.values():
            estructura += subcarpeta.ver_contenido(nivel + 1)
        return estructura

#
class ArchSist:
    def __init__(self):
        self.raiz = Carpeta("root")
        self.actual = self.raiz
        self.ruta = ["root"]

    # --- Ventana dinámica para todas las acciones del sistema ---
    def ver_ventana(self, titulo, mensaje):
        ventana = tk.Tk()
        ventana.title(titulo)  # 🔹 título dinámico según la acción
        ventana.geometry("420x400")

        etiqueta = tk.Label(ventana, text=mensaje, font=("Arial", 11, "bold"), fg="blue")
        etiqueta.pack(pady=10)

        texto = tk.Text(ventana, wrap="word", height=18, width=45)
        texto.insert("1.0", self.raiz.ver_contenido())
        texto.config(state="disabled")
        texto.pack(pady=10)

        boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#FFC1D5")
        boton.pack(pady=5)

        ventana.mainloop(60)

    # --- Opciones del menú ---
    def crear_carpeta(self):
        nombre = input("Nombre de la nueva carpeta: ")
        mensaje = self.actual.crear_subcarpeta(nombre)
        self.ver_ventana("Creación de carpeta", mensaje)

    def mostrar_carpetas(self):
        mensaje = "Árbol de carpetas actuales:"
        self.ver_ventana("Árbol de carpetas", mensaje)

    def eliminar_carpeta(self):
        nombre = input("Nombre de la carpeta a eliminar: ")
        mensaje = self.actual.eliminar_subcarpeta(nombre)
        self.ver_ventana("Eliminación de carpeta", mensaje)

    def ir_a_carpeta(self):
        nombre = input("Nombre de la carpeta a la que desea ir: ")

        # Evitar intentar entrar de nuevo en root
        if nombre.lower() == "root":
            self.actual = self.raiz
            self.ruta = ["root"]
            mensaje = "Ya estás en la carpeta raíz (root)."
        elif nombre == "..":
            # Subir un nivel si no estás en la raíz
            if len(self.ruta) > 1:
                self.ruta.pop()
                carpeta_actual = self.raiz
                # reconstruir la ruta actual correctamente
                for carpeta in self.ruta[1:]:
                    if carpeta in carpeta_actual.subcarpetas:
                        carpeta_actual = carpeta_actual.subcarpetas[carpeta]
                self.actual = carpeta_actual
                mensaje = f"Has regresado a: {'/'.join(self.ruta)}"
            else:
                mensaje = "Ya estás en la carpeta raíz."
        elif nombre in self.actual.subcarpetas:
            # Navegar dentro de una subcarpeta existente
            self.actual = self.actual.subcarpetas[nombre]
            self.ruta.append(nombre)
            mensaje = f"Ahora estás en: {'/'.join(self.ruta)}"

        else:
            mensaje = f"La carpeta '{nombre}' no existe en la carpeta actual."

        # Mostrar ventana siempre con el árbol actualizado
        self.ver_ventana("Ubicación actual", mensaje)



# --- Menú principal ---
def menu():
    sist = ArchSist()

    while True:
        print("\n=== SISTEMA DE ARCHIVOS ===\n")
        print("Ubicación actual:", "/".join(sist.ruta))
        print("1. Crear nueva carpeta")
        print("2. Mostrar carpetas existentes")
        print("3. Eliminar carpeta")
        print("4. Ir hasta una carpeta")
        print("5. Abandonar sistema de archivos\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sist.crear_carpeta()
        elif opcion == "2":
            sist.mostrar_carpetas()
        elif opcion == "3":
            sist.eliminar_carpeta()
        elif opcion == "4":
            sist.ir_a_carpeta()
        elif opcion == "5":
            print("Saliendo del sistema de archivos...")
            break
        else:
            print("Opción no válida, intente otra opción.")


# --- Ejecución ---
if __name__ == "__main__":
    menu()
