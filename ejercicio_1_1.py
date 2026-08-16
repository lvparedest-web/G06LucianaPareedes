
a="Carlo Jose Luis"
#a
print(a[0])
print(a[1])
print(a[4])
print(a[10])
print(a[-1])
#b
n=len(a)
print(a[0])
print(a[n-1])
#c
print(a[-1])
print(a[-n])
#d
print(a[n])          
print(a[-n-1])
#e
print(a[1.5])
print(a[1.0])

#d
#Error porque a[n] = a[15], pero el último índice es 14
#También a[-n-1] = a[-16], y ese índice no existe
#Por eso Python genera IndexError
#e
#Error porque los índices deben ser números enteros
#1.5 y 1.0 son números decimales (float)
#Por eso Python genera TypeError
