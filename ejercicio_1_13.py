#a)
a=[1,2,3]
b=a
c=a[:]   #realiza una copia de la lista "a"
a[0]=4
print(a)
print(b)
print(c)

#b)
def f(a):
    b=a[:]
    b.append(1)
    return b
#main
a=[2]
b=f(a)
print(a)
print(b)
