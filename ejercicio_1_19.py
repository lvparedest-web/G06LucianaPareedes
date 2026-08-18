#a) Determinar el tipo en b = [1, 2, 3] y encontrar:
#-i) str(b)
b=[1, 2, 3]
print(type(str(b)))
print(str(b))
#ii) tuple(b)
b=[1, 2, 3]
print(type(tuple(b)))
print(tuple(b))
#iii) list(b)
b=[1, 2, 3]
print(type(list(b)))
print(list(b))

#b) Si c = (1, 2, 3), comprobar si tuple(list(b)) es c.
c=(1, 2, 3)
print(tuple(list(b)))    #sí es igual a c porque ambas son tuplas

#c) De la misma forma, ver que cuando b = [1, 2, 3], entonces list(tuple(b)) es b.
b=[1, 2, 3]
print(list(tuple(b)))

#d) Determinar el tipo de c = 'Ana Paula' y encontrar:
c="Ana Paula"
print(type(c))
#i) str(c)
print(str(c))
#ii) tuple(c)
print(tuple(c))
#iii) list(c)
print(list(c))
#iv) ¿Es verdad que str(list(c)) es c?
if (str(list(c)))==c:
    print(True)
else:
    print(False)
