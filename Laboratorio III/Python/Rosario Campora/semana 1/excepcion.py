class NumerosIdenticosExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.message = mensaje

resultado = None

try:
    numero1 = int(input('Ingrese el primer número: '))
    numero2 = int(input('Ingrese el segundo número: '))
    if numero1 == numero2:
        raise NumerosIdenticosExcepcion('Los números son idénticos')
    resultado = numero1 / numero2
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except NumerosIdenticosExcepcion as e:
    print(f'NumerosIdenticosExcepcion - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Excepción general - Ocurrió un error: {type(e)}')
else:
    print("No se arrojó ninguna excepción")
finally:
    print("Se ejecuta este bloque finally")

print(f'El resultado es: {resultado}')
print('Continuará...')
