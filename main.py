#prueba roberto
#prueba fernando
#prueba luis

from datetime import date
from libro import Libro
from usuario import Usuario
from Datos import libros
from Datos import usuarios

from biblioteca import Biblioteca

#lista_libros=[]
#for id_libro, datos in libros.items():
#    libro = Libro(id_libro, datos["titulo"], datos["autor"])
#    lista_libros.append(libro)

#lista_usuarios=[]
#for datos in usuarios.values():
#    usuario = Usuario(datos["id_usuario"],datos["nombre"])
#    lista_usuarios.append(usuario)

#for libro in lista_libros:
#    print (libro)
#for usuario in lista_usuarios:
#    print (usuario)

#usuario1.pedirLibro(libro1) 
#usuario2.pedirLibro(libro1)
#usuario1.devolver_libro(libro1)
#usuario2.pedirLibro(libro1)


bibioteca = Biblioteca()
bibioteca.menu()