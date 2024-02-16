# Crear un menu para un registro de pasajeros
pasajeros = {}
def menu ():
    global pasajeros
    opcion= int ( input( """Sistema de regristro de pasajes
[1] registras pasajeros
[2] listar pasajeros
[3] borrar data
[4] salir
coloca un numero """))
    if opcion == 1:
        nombre= input("Escribe el nombre del pasajero: " )
        cedula= input("Escribe la cedula del pasajero: " )
        asiento = input("asigna el del pasajero: " )
        pasajeros [asiento] = [ nombre,cedula]
    elif opcion == 2:
        if len(pasajeros.items())==0:
            print("no hay pasajeros")
        for llave, valor in pasajeros.items():
             print ("el asiento: ", llave, "le corresponde a: ", valor [0] )
    elif opcion == 3:
        pasajeros= {}
    elif opcion == 4:
        quit()
    menu()

        
menu()