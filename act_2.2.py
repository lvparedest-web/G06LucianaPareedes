lista=[]
num1=num2=num_apar=x=suma=0
num1=int(input("Ingrese cuantos números tiene la lista: "))
for i in range(0,num1):
    x=int(input("Ingrese un número: "))
    lista.append(x)
print("La lista es: ", lista)
num2=int(input("Ingrese el número a buscar: "))
for y in range(0,num1):
    if lista[y]==num2:
        num_apar=num_apar+1
        suma=suma+lista[y]
print("El número ", num2, " aparece ", num_apar, "veces")
print("La sumatoria del número ", num2, " es: ", suma)

    

