import flet

# Calcular el area de un circulo
def AreaCirculo ():
    r= int (input("radio:"))
    PI=3.1416
    area= PI*r**2
    print("El area es:", area)

AreaCirculo()