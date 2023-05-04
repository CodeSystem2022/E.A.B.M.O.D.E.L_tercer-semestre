try:
    # Código que podría generar una excepción
    x = int(input("Introduce un número: "))
    y = 1 / x
    print(f"El resultado es {y}")
except ValueError:
    print("Debes introducir un número entero.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except:
    print("Ha ocurrido un error inesperado.")
