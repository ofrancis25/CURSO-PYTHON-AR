#Crear un Promedio de una lista de numeros

def promedio_lista():
    lista_numeros=[]
    cantidad_num=int (input("la cantidad de numero que quiero: "))
    for i in range (cantidad_num):
        numero=int (input("el numero que quiero: " ))
        lista_numeros.append(numero)
    suma = 0
    for i in lista_numeros:
        suma+=i
    promedio= suma / cantidad_num
    return promedio
resultado= promedio_lista()
print("el promedio es:",resultado)