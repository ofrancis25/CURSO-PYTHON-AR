# calcular el factorial de un numero
def Factorial(num):
    Factorial=1
    for numero in range (1,num+1):
        Factorial*=numero
        print("El Factorial de", num,"es:", Factorial)  
Factorial(5)
Factorial(7)  
    