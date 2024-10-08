from prestamo import Prestamo
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
    
    def __str__(self):
        return f"ID: {self.id_usuario} | Nombre: {self.nombre}"