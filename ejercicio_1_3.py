#a)
a=(456, "mi papa", 789)
#i. Encontrar el valor, el tipo (con type) y la longitud (con len) de a.
print("Valor: ", a)
print("Tipo: ", type(a))
print("Longitud: ",len(a))

#ii. ¿Cuál sería el resultado de a[1] y de a[20]?
print(a[1])
#print(a[20])   #generae un error porque sale del índice

#b)
#i. En la terminal escribir a = (6) y verificar el valor y tipo de a.
a=(6)
print("Valor: ",a)
print("Tipo: ", type(a))

#ii. Repetir para a = (6,).
a=(6,)
print("Valor: ",a)
print("Tipo: ",type(a))

#c)
a=()
#i. Encontrar su valor, tipo y longitud.
print("Valor: ",a)
print("Tipo: ",type(a))
print("Longitud: ",len(a))

#ii. Comparar los resultados de a = (,) y de a = , con los del ejercicio b).
#a=(,)     Genera un error de sintaxis
#b=,       porque la forma correcta de crear una tupla vacia es a=()

#d)
a,b = 3,"tu papa"
print(a)
print(b)
print(a,b)
