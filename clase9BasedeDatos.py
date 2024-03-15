#base de datos
import sqlite3
conn= sqlite3.connect("bd_clase9.sqlite3")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Estudiante( Nombres TEXT PK, Curso TEXT)")
""" cursor.execute("INSERT INTO Estudiante VALUES ('Daniel', '6to')")
cursor.execute("INSERT INTO Estudiante VALUES ('Juan', '2do')")
cursor.execute("INSERT INTO Estudiante VALUES ('Salomon', '3ero')")
cursor.execute("INSERT INTO Estudiante VALUES ('Francelis', '4to')")
cursor.execute("INSERT INTO Estudiante VALUES ('Eliezer', '1ero')") """
cursor.execute(" SELECT *FROM Estudiante")

cursor.execute("DELETE FROM Estudiante WHERE Nombres= 'Daniel'")
conn.commit()
cursor.execute("UPDATE Estudiante SET Curso= '2do' WHERE Nombres= 'Francelis'")
conn.commit()
res=cursor.execute(" SELECT *FROM Estudiante")
data= res.fetchall()
for valor in data:
    print(f"Nombre: {valor[0]}, Curso:{valor[1]}")

