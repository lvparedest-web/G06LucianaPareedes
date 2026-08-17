def f(a):
    """Agregar 1 a la lista"""
    a.append(1)
#main
a=[2]
b=a
f(a)
print(b)
"""Porque en el programa principal se determina que "a" tiene un elemento, 2,
y que "b" y "a" hacen referencia a la misma lista, entonces el valor añadido
a la lista "a" en la función, también se agrega a "b".
