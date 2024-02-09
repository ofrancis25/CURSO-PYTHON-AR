""" buscar en una lista un valor ingresado por el usuario y devolver su posicion en la lista"""
texto = input("Ingrese un texto: ")
valor= input("Ingrese una letra a buscar del texto ingresado: ")
n = len(texto) #len(texto) devuelvela longitud total de la cadena
encontrado = []

for i in range(n):
    if(texto[i] == valor):
        encontrado.append(i)
        
print("La posicion o posiciones donde se encentra la letra (", valor, ") es o son: ",encontrado)
        