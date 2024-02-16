#Calcular un numero primo
def es_primo():
    numero= int (input("Introduce un numero: " ))
    for i in range (2, numero):
        if numero % i == 0:
            print ("no es primo")
            return
        print ("si es primo")
        
es_primo()