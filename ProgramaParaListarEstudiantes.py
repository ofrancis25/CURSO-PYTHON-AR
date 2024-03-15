#Listar Estudiantes
import sqlite3
conn= sqlite3.connect("bd_clase9.sqlite3")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Estudiantes( Nombres TEXT PK)")

def menu ():
    global Estudiantes
    opcion = int (input ("""Sistema de regristro de Estudiantes
[1] registras Estudiantes
[2] listar Estudiantes
[3] borrar data
[4] salir
coloca un numero """))
    if opcion == 1:
        nombre= input("Escribe el nombre del Estudiante: " )
        cedula= input("Escribe la cedula del Estudiante: " )
        Curso = input("asigna Grado del Estudiante: " )
    elif opcion == 2:
        if len(Estudiante.items())==0:
            print("no hay Estudiante")
        for llave, valor in Estudiante.items():
             print ("el Estudiante: ", llave, "le corresponde al Curso: ", valor [0] )
    elif opcion == 3:
        Estudiante= {}
    elif opcion == 4:
        quit()
    
    menu()
menu()

        
    
