class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer_archivo(self):
        self.archivo = open(self.nombre, 'r', encoding='utf-8')
        return self.archivo.read()

    def escribir_archivo(self, contenido):
        archivo_destino = open('copia.txt', 'w', encoding='utf-8')
        archivo_destino.write(contenido)
        archivo_destino.close()

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        return self

    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print('Cerramos el recurso'.center(50, '-'))
        if self.archivo:
            self.archivo.close()


with ManejoArchivos('prueba.txt') as ma:
    contenido = ma.leer_archivo()
    print(contenido)
    ma.escribir_archivo(contenido)

print('Se leyó y se copiaron los archivos')
