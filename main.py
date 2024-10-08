#prueba roberto
#prueba fernando
#prueba luis

from datetime import date
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

libro1 = Libro(1, "1984", "George Orwell")
libro2 = Libro(2, "Cien años de soledad", "Gabriel García Márquez")
usuario1 = Usuario(1, "Juan Pérez")
usuario2 = Usuario(2, "Ana López")

usuario1.pedirLibro(libro1) 
usuario2.pedirLibro(libro1)
usuario1.devolver_libro(libro1)  # Juan devuelve "1984"
usuario2.pedirLibro(libro1)  # Ana ahora puede pedir "1984"