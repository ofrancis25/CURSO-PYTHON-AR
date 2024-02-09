#clacular el total de la compra
lista_compras = []
cant_datos = int (input("Ingresa la cantidad de datos: "))

for i in range(cant_datos):
    valor = int (input("Ingresed el valor #" + str(i+1)))
    lista_compras.append(valor)
    
print (lista_compras)
total = 0

for precio in lista_compras:
    total += precio
print (total)