class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestamo = False

    def prestarlibro(self):
        if not self.prestamo:  # Si no está prestado
            self.prestamo = True  # Cambia estado a prestado
        else:
            print("El libro ya está prestado.")

    def devolverlibro(self):
        if self.prestamo:
            self.prestamo = False  # Cambia estado a disponible
        else:
            print("El libro no está prestado.")

    def __str__(self):
        estado = "No Disponible" if self.prestamo else "Disponible"
        return f"ID: {self.id_libro} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"