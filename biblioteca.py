
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo
from Datos import libros
from Datos import usuarios

class Biblioteca:
    def __init__(self):
        self.libros = [Libro(datos["id_libro"], datos["titulo"], datos["autor"]) for datos in libros.values()]
        self.usuarios = {datos["id_usuario"]: Usuario(datos["id_usuario"], datos["nombre"]) for datos in usuarios.values()}
        self.prestamos = []

    def agregar_libro(self, id_libro, titulo, autor):
        libro = Libro(id_libro, titulo, autor)
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        print("Libros disponibles:")
        for libro in self.libros:
            print(libro)
    
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios creados.")
            return
        print("Usuarios creados:")
        for usuario in self.usuarios:
            print(usuario)

    def solicitar_prestamo(self, id_usuario, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                libroSeleccionado = libro
            else:
                libroSeleccionado = None
        #libro = next((libro for libro in self.libros if libro.id_libro == id_libro), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)

        libro = next((libro for libro in self.libros if libro.id_libro == id_libro), None)
        if libro is None:
            print(f"El libro con ID {id_libro} no existe.")
            return
        
        if usuario is None:
            print("El usuario no existe.")
            return
        if libro in [prestamo.libro for prestamo in self.prestamos]:
            print("El libro ya está prestado.")
            return

        prestamo = Prestamo(usuario, libro)
        self.prestamos.append(prestamo)
        print(f"Préstamo realizado: {prestamo}")

    def devolver_libro(self, id_usuario, id_libro):
        prestamo = next((p for p in self.prestamos if p.libro.id_libro == id_libro and p.usuario.id_usuario == id_usuario), None)

        if prestamo:
            self.prestamos.remove(prestamo)
            print(f"Libro devuelto: {prestamo.libro}")
        else:
            print("No existe un préstamo registrado para este libro y usuario.")

    def menu(self):
        while True:
            print("\n--- Menú de Biblioteca ---")
            print("1. Agregar libro")
            print("2. Mostrar libros")
            print("3. Solicitar préstamo")
            print("4. Devolver libro")
            print("5. Mostrar usuarios")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_libro = input("Ingrese ID del libro: ")
                titulo = input("Ingrese título del libro: ")
                autor = input("Ingrese autor del libro: ")
                self.agregar_libro(id_libro, titulo, autor)
            elif opcion == "2":
                self.mostrar_libros()
            elif opcion == "3":
                id_usuario = input("Ingrese ID del usuario: ")
                id_libro = int(input("Ingrese ID del libro: "))
                self.solicitar_prestamo(id_usuario, id_libro)
            elif opcion == "4":
                id_usuario = input("Ingrese ID del usuario: ")
                id_libro = input("Ingrese ID del libro: ")
                self.devolver_libro(id_usuario, id_libro)
            elif opcion == "5":
                self.mostrar_usuarios()
            elif opcion == "6":
                print("Saliendo del sistema. ¡Gracias por usar la Biblioteca!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
