colores=["rojo", "azul", "verde", "amarillo", "morado"]
print("La lista tiene ", len(colores), " colores")
x=1
x=int(input("Ingrese el número de color: "))
if x<6 and x>0:
    print("El color ", x, "es: ", colores[x-1])
else:
    print("Imposible")
