import os
    
class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre} \n')
    
    @classmethod
    def listar_pelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf-8') as archivo:
            print('CatalogoPeliculas'.center(50,'-'))
            print(archivo.read())
        
    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'archivo eliminado: {cls.ruta_archivo}')
        