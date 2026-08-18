#a) Escribir el comando a = [4, 2, 13] y verificar el valor de a.
a = [4, 2, 13]
print(a)
#b) Escribir a[0] = 5 y volver a verificar el valor de a.
a[0] = 5
print(a)
#c) Escribir c = a y verificar el valor de c.
c = a
print(c)
#d) Escribir a[0] = 4 y verificar los valores de a y c.
a[0] = 4
print(a)
print(c)
#e) Escribir a = [7, 28, 9] y verificar los valores de a y c
a = [7, 28, 9]
print(a)
print(c)
#f) Cambiar a tuplas los ejercicios de listas anteriormente resueltos , osea,
#comenzando con a = 11,12, 13 y ver los erorres que se producen.

a = (11,12, 13)
print(a)
a[0] = 5
print(a)
c = a
print(c)
a[0] = 4
print(a)
print(c)
a = (7, 28, 9)
print(a)
print(c)
#las tuplas son inmutables, por lo que no permiten modificar
#directamente sus elementos y Python genera un TypeError al intentar hacerlo
