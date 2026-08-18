#a) Para determinar si x es un número entero o real, se escribe:
"""x = 10
if isinstance(x, (int, float)):
 print("x es número entero o real")
else:
 print("x no es número")
Evaluar cuando x vale:
"""
#i) 11
if isinstance(11, (int, float)):
    print("x es número entero o real")
else:
    print("x no es número")
#ii) 11.2
if isinstance(11.2, (int, float)):
    print("x es número entero o real")
else:
    print("x no es número")
#iii) ’tu mama’
if isinstance("tu mamá", (int, float)):
    print("x es número entero o real")
else:
    print("x no es número")
#iv) True
if isinstance(True, (int, float)):
    print("x es número entero o real")
else:
    print("x no es número")
#b) Crear la función es_secuencia para saber si su argumento es o no una secuencia
#(cadena, tupla, lista o rango).
def es_secuencia(x):
    if isinstance(x, (str, tuple, list, range)):
        return True
    else:
        return False
print(es_secuencia("hola"))
print(es_secuencia((1, 2, 3)))
print(es_secuencia([1, 2, 3]))
print(es_secuencia(range(5)))
print(es_secuencia(25))
