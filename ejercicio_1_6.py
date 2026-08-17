#a)
#i. Volver a hacer el ejercicio 1.3.a)
a = [456, "mi papa", 789]
print("Valor: ", a)
print("Tipo: ", type(a))
print("Longitud: ",len(a))
print(a[1])
#ii. Obtener la cadena ’mi papá’ de a, luego obtener la ’i’ en ’mi papá’?
print(a[1])
print(a[1][1])

#b)
#Hallar el valor, el tipo y la longitud de a si:
#i
a = []
print("Valor: ", a)
print("Tipo: ", type(a))
print("Longitud: ",len(a))
#ii
a = [4]
print("Valor: ", a)
print("Tipo: ", type(a))
print("Longitud: ",len(a))
#iii
a = [6,]
print("Valor: ", a)
print("Tipo: ", type(a))
print("Longitud: ",len(a))

#c)
#¿De las siguientes cuales son secuencias y cuáles no?, ¿Por qué?
#i.
a=(7)
print(type(a))    #Es un número, no una secuencia
#ii.
a=(7,)
print(type(a))    #Es una secuencia porque es una tupla
#iii.
a=[7]
print(type(a))  #Es una secuencia porque es una lista
#iv.
a=[7,]
print(type(a))    #Es una secuencia porque es una lista

#d)
#Ver los resultados de los siguientes
#comandos y verificar los tipos de las variables x e y:
x = a,b = [6, 5]
print(x)
print(type(x))     #Es una lista
y = [a, b] = 5, 6
print(y)
print(type(y))     #Es una tupla

#e)
#i.En la computadora escribir [c, d] = [5, 7] y verificar los valores de c y d.
[c, d] = [5, 7]
print(c)
print(d)
#ii.Escribir [c, d] = [d, c] y volver a verificar los valores de c y d.
[c, d] = [d, c]
print(c)
print(d)

