#a)
#Investigar qué hace la función divmod y evaluar con distintos valores.

print("Ejemplo 1: ")
a=divmod(10,3)
print(a)
print("Ejemplo 2: ")
b=divmod(25,4)
print(b)
print("Ejemplo 3: ")
c=divmod(100,4)
print(c)

#b)
#Con r y s, implementar una función que retorne la tupla (r, s) para luego ver los resultados
#de divmod con entradas positivas y negativas.
def mi_divmod(r, s):
    return divmod(r, s)
print(mi_divmod(10, 3))
print(mi_divmod(-10, 3))
print(mi_divmod(10, -3))
print(mi_divmod(-10, -3))
