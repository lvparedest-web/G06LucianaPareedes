#a)
a=[1,[2,3]]
b=a[:]
a[1][1]=4
print(a)
print(b)

#b)
a=[1,[2,3]]
b=a
a[1][1]=4
print(b)
