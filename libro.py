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

    def __str__(self):
        if self.prestamo:
            estado = "No Disponible"
        else:
            estado = "Disponible"
        return f"ID: {self.id_libro} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"