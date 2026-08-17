b=["p", "r", "o", "c", "e", "d", "i", "m","i","e","n","t","o"]
#a)¿Cuántos elementos tiene a?, ¿Cuál es el valor de b[3]?
print(len(b))
print(b[3])

#b)Verificar el valor resultante de b y su longitud con len(b)
#i. b.append("c")
b.append("c")     #agrega un valor
print(b)
print(len(b))
#ii. b.pop()
b.pop()     #elimina el último valor
print(b)
print(len(b))
#iii. b.pop(0)
b.pop(0)     #elimina un valor según su índice
print(b)
print(len(b))
#iv. b.insert(4, ’w’)
b.insert(4,"w")     #inserta un valor según el índice sin reemplazo
print(b)
print(len(b))
#v. b.insert(-1, ’h’)
b.insert(-1, "h")    #inserta un valor según el índice negativo sin reemplazo
print(b)
print(len(b))
#vi. b.reverse()
b.reverse()     #voltea el orden de los elementos de la lista
print(b)
print(len(b))
