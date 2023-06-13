from nroiden import NumerosIdenticosExcepcion

resultado = None

try:
    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))
    if num1 == num2:
        raise NumerosIdenticosExcepcion('Los números son iguales')
    resultado = num1 / num2
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except NumerosIdenticosExcepcion as e:
    print(f'NumerosIdenticosExcepcion - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Excepción general - Ocurrió un error: {type(e)}')
else:
    print("ninguna excepción")
finally:
    print("Se ejecuta finally")

print(f'El resultado es: {resultado}')
