a = "Juan Armando y Luren Amelia"
#i)
print(a[0:4])
#ii)
print(a[1:5])
#iii)
print(a[6:6])
#iv)
print(a[3:])
#v)
print(a[:5])
#vi)
print(a[:])
#vii)
print(a[-1:4])
#viii)
print(a[4:-1])
print(a)     #a no cambia
#¿Es posible predecir el resultado de a == a[:7] + a[7:]?
print(a == a[:7] + a[7:])
#Sí, porque se parte de una cadena en 2 y al juntarla se obtiene de nuevo la cadena
#i)
print(a[2:99])
#ii)
print(a[99:2])  #Se obtiene una cadena vacía aunque el índice este fuera del rango
#iii)
print(a[-99:2])
#iv)
print(a[-99:99])      
#a. ¿Qué índices habrá que utilizar para obtener ’Luren’?
print(a[15:21])
#b. Encontrar u, y, v, x de modo a[u:v] + a[x:y] sea ’Juan y Luren’
print(a[0:4] + a[12:21])
#c. Ver qué hacen las instrucciones:
#i)
print(a[0:10:2])
#ii)
print(a[:10:2])
#iii)
print(a[-10::2])
#iv)
print(a[::2])
#v)
print(a[::-1])

