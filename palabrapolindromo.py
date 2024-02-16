# Calcular una palabra polindromo
def palabra_polindromo():
    palabra= input ("escribe una palabra: " )
    palabra_inv= palabra [::-1]
    if palabra == palabra_inv:
        print ("si es polindromo")
    else:
        print ("no es polindromo")

palabra_polindromo()