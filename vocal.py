#ir letra por letra de un texto para saber cuantas voales tiene

texto = input("ingresa un texto: ")

cant_vocales =0
for i in texto:
    letra=i
    if letra in ["a","A","e","E","i","I","o","O","u","u"]:
        cant_vocales +=1
        
print("La cantidad de vocales en la palabra es: ",cant_vocales)
         
         """((letra == "a") or(letra == "A") or (letra == "e") or  (letra == "E") or (letra == "i") or (letra == "I") or  (letra == "o") or (letra == "O") or (letra == "u") or (letra == "U")):"""