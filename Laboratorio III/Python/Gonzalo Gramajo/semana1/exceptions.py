from numeros_iguales_excepciones import NumerosIgualesExcepciones


def division(num1, num2):
    resultado = None
    try:
        resultado = num1/num2
        if num1 == num2:
            raise NumerosIgualesExcepciones("los numeros son iguales")
    except ZeroDivisionError as e:
        print(f"\nuna excepcion ocurrio: {e}")
    except Exception as e:
        print(f'\nuna excepcion ocurrio: {e}')    
    else:
        print("\nno se arrojo una excepcion")
    finally:
        print("se muestra la ejecucion del bloque finally")
    return resultado



if __name__ == "__main__":
    print(division(7,2),end="\n"+"*****"*20)
    print(division(7,0),end="\n"+"*****"*20)
    print(division('a',7),end="\n"+"****"*20)
    print(division(7,7),end="\n"+"****"*20)
    