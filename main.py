#prueba roberto
#prueba fernando
#prueba luis

from datetime import date

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestamo = False

    def prestarlibro(self):
        if not self.prestamo: #si no es verdadero prestar
            self.prestamo =True # cambia estado a prestado
        else:
            print("El libro ya está prestado")

    def devolverlibro(self):
        if self.prestamo: 
            self.prestamo =False
        else:
            print("el libro no está prestado")

class Usuario:
    def __init__(self, id_usuario,nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []
    
    def pedirLibro(self,libro):
        if libro.prestamo == True:
            print (f"{libro.titulo} esta prestado")
        else:
            prestamo = Prestamo(self,libro)
            prestamo.realizarPrestamo()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} a pedido prestado el libro {libro.titulo}")
    
    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            libro.devolverlibro()
            self.libros_prestados.remove(libro)  # Retiramos el libro de la lista de préstamos
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' en préstamo.")

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = None
        self.ocupado = False

    def realizarPrestamo(self):
        if not self.ocupado:
            self.libro.prestarlibro()
            self.fecha_prestamo = date.today()  # Establecemos la fecha del préstamo
            self.ocupado = True
            print(f"Préstamo realizado: {self.libro.titulo} prestado a {self.usuario.nombre} el {self.fecha_prestamo}.")
        else:
            print(f"El préstamo ya está activo.")

    def finalizar_prestamo(self):
        if self.ocupado:
            self.libro.devolverlibro()
            self.ocupado = False
            print(f"Préstamo finalizado: {self.libro} devuelto por {self.usuario}.")
        else:
            print("No hay préstamo activo.")


libro1 = Libro(1, "1984", "George Orwell")
libro2 = Libro(2, "Cien años de soledad", "Gabriel García Márquez")
usuario1 = Usuario(1, "Juan Pérez")
usuario2 = Usuario(2, "Ana López")

usuario1.pedirLibro(libro1) 
usuario2.pedirLibro(libro1)
usuario1.devolver_libro(libro1)  # Juan devuelve "1984"
usuario2.pedirLibro(libro1)  # Ana ahora puede pedir "1984"