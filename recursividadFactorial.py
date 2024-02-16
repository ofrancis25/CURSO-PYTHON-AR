# Calcular el factorial de un numero
def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial (n-1)

num= int(input())    
resultado= factorial(num)
print (resultado)
