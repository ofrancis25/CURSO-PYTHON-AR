#Calcular el minimo comum multiplo de un numero
def mcm_numero():
    num1= int (input ("Introduce num1: "))
    num2= int(input ("Introduce num2: " ) )
    if num1 > num2:
            control = num1
    else:
            control = num2
    while True:
        if control % num1==0 and control % num2==0:
            print ( "el mcm es:", control)
            break
        control+= 1
        
mcm_numero()