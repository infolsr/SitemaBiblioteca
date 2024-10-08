#prueba roberto
#prueba fernando
#prueba luis

from datetime import date
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

libro1 = Libro(1, "Mujeres del Alma Mia", "Isabel Allende")
libro2 = Libro(2, "Palomita Blanca", "Enrique Lafourcade")
usuario1 = Usuario(1, "Luis Gonzalez")
usuario2 = Usuario(2, "Roberto Maya")
usuario3 = Usuario(3, "Fernando Godoy")

usuario1.pedirLibro(libro1) 
usuario2.pedirLibro(libro1)
usuario1.devolver_libro(libro1)
usuario2.pedirLibro(libro1)