class Pelicula:
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return f'P : {self.name}'

    @property
    def nombre(self):
        return self._name

    @nombre.setter
    def nombre(self, value):
        self._name = value
    