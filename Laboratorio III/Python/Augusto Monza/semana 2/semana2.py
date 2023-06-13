class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')#Encapsulamos el código dentro del método
        return self.nombre
    
    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

archivo = open('prueba.txt', 'r', encoding = 'utf-8')

archivo2 = open('copia.txt', 'w', encoding= 'utf-8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se leyó y se copió archivos')