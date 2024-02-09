PI=3.1416
radio= float (input("ingresa el radio:"))
h= float (input("ingresa la altura:"))
volumen= PI*(radio**2)*h
area_base= PI*(radio**2)
area_curva= 2*PI*radio*h
area=area_base+area_curva
print ("El area del cilindro es:", area, "y el volumen del cilindro es:", volumen)