class ManejoArchivos:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def __enter__(self):
        self.nombre = open(self.nombre, 'r', encoding = 'utf8')  # encapsulamos el codigo
        return self.nombre
    
    def __exit__(self, tipo_exception, valor_excepcion, traza_error):
        if self.nombre:
            self.nombre.close()  #cerramos el archivo
