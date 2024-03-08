libros={}
def menu():
    global libros
    opc=int(input(""" Registro de Biblioteca
            [1] Registrar
            [2] Libros 
            [3] Borrar data 
            [4] Salir      
            elija una opcion: """))
    if opc==1:
      nombre=input("introduzca su nombre: ")
      libro=input("que libro desea solicitar?: ")
      print('Datos guardados con exito \n')
      
      libros[libro]=[nombre]
    elif opc==2:
       if len(libros)==0:
           print("No hay registros disponibles")
       for llave, valor in libros.items():
          print("El libro: ", llave, "fue prestado a: ", valor[0])
    elif opc==3:
       libros={}
    elif opc==4:
       quit()
    menu()          
menu()          