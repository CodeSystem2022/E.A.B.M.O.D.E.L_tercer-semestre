from manejo_archivos import ManejoArchivos
# manejo de contexto with


with ManejoArchivos('text.txt') as m:
    print(m.read())
    
