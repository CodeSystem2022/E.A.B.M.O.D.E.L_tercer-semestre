from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as Cp

opcion = None
while opcion != 4:
    try:
        print('opciones: ')
        print('1/ Agregar peliculas')
        print('2/ Listar peliculas')
        print('3/ Eliminar catalogo de peliculas')
        print('4/ salir')
        opcion = int(input('Escribe tu opcion: '))
        if opcion == 1:
            nombre_pelicula = input('Nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            Cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            Cp.listar_pelicula()
        elif opcion == 3:
            Cp.eliminar_pelicula()
        
    except Exception as e:
        print(f'error: {e}')
        opcion = None
else:
    print('salimos del programa')