from datetime import date
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = None
        self.ocupado = False

    def realizarPrestamo(self):
        if not self.ocupado:
            if not self.libro.prestamo:  # Verifica si el libro está disponible
                self.libro.prestarlibro()  # Realiza el préstamo
                self.fecha_prestamo = date.today()  # Establece la fecha del préstamo
                self.ocupado = True
                print(f"Préstamo realizado: '{self.libro.titulo}' prestado a {self.usuario.nombre} el {self.fecha_prestamo}.")
            else:
                print(f"No se puede realizar el préstamo, el libro '{self.libro.titulo}' ya está prestado.")
        else:
            print("El préstamo ya está activo.")

    def finalizar_prestamo(self):
        if self.ocupado:
            self.libro.devolverlibro()  # Cambia el estado del libro a disponible
            self.ocupado = False
            print(f"Préstamo finalizado: '{self.libro}' devuelto por {self.usuario}.")
        else:
            print("No hay préstamo activo.")