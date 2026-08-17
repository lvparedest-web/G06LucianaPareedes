#a)
#Verificar los valores de a y b luego de escribir en la terminal:
a,b = 1,2
print(a)
print(b)

#b)
#Escribir: a, b = b, a y verificar finalmente los valores de a y b.
a,b = b,a
print(a)
print(b)

#c)
#Operaciones combinando con el intercambio:
a, b = 5, 7
print(a)
print(b)
a, b = a - b, a + b
print(a)
print(b)
a,b = b,a
print(a)
print(b)

#d)
#En la función mcd2 siguiente modificar las instrucciones
#r=a%b
#a=b
#b=r
#por un único reglón de forma que el resultado no varíe.
def mcd2(a,b):
    a=abs(a)
    b=abs(b)
    while b!=0:
        a,b=b,a%b
    return a
print(mcd2(48,18))
