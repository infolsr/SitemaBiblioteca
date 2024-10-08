#prueba roberto
#prueba fernando
#prueba luis

class libro:
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

class usuario:
    def __init__(self, id_usuario,nombre,):
        self.id_usuario = id_usuario
        self.nombre = nombre
    
    def pedirLibro(self,libro):
        if libro.prestamo == True:
            print (f"{libro.titulo} esta prestado")
        else:
            Prestamo = prestamo(libro)
            Prestamo = realizarPrestamo
    

class prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = None
        self.ocupado = False


