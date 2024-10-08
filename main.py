#prueba roberto
#prueba fernando
#prueba luis

class libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestamo = False
        

class usuario:
    def __init__(self, id_usuario,nombre,):
        self.id_usuario = id_usuario
        self.nombre = nombre

class prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = None
        self.ocupado = False


