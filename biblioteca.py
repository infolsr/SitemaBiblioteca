
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo
from Datos import libros
from Datos import usuarios

class Biblioteca:
    def __init__(self):
        # Cambiamos a diccionarios, donde las claves son los IDs
        self.libros = {datos["id_libro"]: Libro(datos["id_libro"], datos["titulo"], datos["autor"]) for datos in libros.values()}
        self.usuarios = {datos["id_usuario"]: Usuario(datos["id_usuario"], datos["nombre"]) for datos in usuarios.values()}
        self.prestamos = []

    def agregar_libro(self, id_libro, titulo, autor):
        libro = Libro(id_libro, titulo, autor)
        self.libros[id_libro] = libro  # Guardar libro en el diccionario
        print(f"Libro agregado: {libro}")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        print("Libros disponibles:")
        for libro in self.libros.values():
            print(libro)
    
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios creados.")
            return
        print("Usuarios creados:")
        for usuario in self.usuarios.values():
            print(usuario)

    def solicitar_prestamo(self, id_usuario, id_libro):
        # Buscar el libro en el diccionario de libros
        libroSeleccionado = self.libros.get(id_libro)
        
        # Buscar el usuario en el diccionario de usuarios
        usuarioSeleccionado = self.usuarios.get(id_usuario)

        # Validaciones de existencia de libro y usuario
        if libroSeleccionado is None:
            print(f"El libro con ID {id_libro} no existe.")
            return
        
        if usuarioSeleccionado is None:
            print(f"El usuario con ID {id_usuario} no existe.")
            return
        
        # Verificar si el libro ya está prestado
        if libroSeleccionado in [prestamo.libro for prestamo in self.prestamos]:
            print("El libro ya está prestado.")
            return

        # Crear el préstamo y asignarlo
        prestamo = Prestamo(usuarioSeleccionado, libroSeleccionado)
        prestamo.realizarPrestamo()
        self.prestamos.append(prestamo)
        print(f"Préstamo realizado: {prestamo}")

    def devolver_libro(self, id_usuario, id_libro):
    # Buscar el préstamo existente
        prestamo = next((p for p in self.prestamos if p.libro.id_libro == id_libro and p.usuario.id_usuario == id_usuario), None)

        if prestamo:
            # Finalizar el préstamo, lo que cambiará el estado del libro a disponible
            prestamo.finalizar_prestamo()
            self.prestamos.remove(prestamo)
            print(f"Libro devuelto: {prestamo.libro.titulo} por {prestamo.usuario.nombre}.")
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
                id_libro = int(input("Ingrese ID del libro: "))  # Convertir el ID a int
                titulo = input("Ingrese título del libro: ")
                autor = input("Ingrese autor del libro: ")
                self.agregar_libro(id_libro, titulo, autor)
            elif opcion == "2":
                self.mostrar_libros()
            elif opcion == "3":
                id_usuario = int(input("Ingrese ID del usuario: "))  # Convertir el ID a int
                id_libro = int(input("Ingrese ID del libro: "))
                self.solicitar_prestamo(id_usuario, id_libro)
            elif opcion == "4":
                id_usuario = int(input("Ingrese ID del usuario: "))  # Convertir el ID a int
                id_libro = int(input("Ingrese ID del libro: "))
                self.devolver_libro(id_usuario, id_libro)
            elif opcion == "5":
                self.mostrar_usuarios()
            elif opcion == "6":
                print("Saliendo del sistema. ¡Gracias por usar la Biblioteca!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

