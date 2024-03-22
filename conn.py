#esto es una prueba
import sqlite3
db = sqlite3.connect ("db.sqlite3",check_same_thread=False)
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tareas(Id INTEGER PRIMARY KEY AUTOINCREMENT, Nombres TEXT, Descripcion TEXT)")

def crearTarea(Nombre, Descripcion):
    cursor.execute("INSERT INTO Tareas (Nombres,Descripcion) VALUES (?, ?)", (Nombre, Descripcion))
    db.commit()

def editarTarea(Id, Nombre, Descripcion):
    cursor.execute("UPDATE Tareas SET Nombres= ?, Descripcion=? WHERE Id= ?", (Nombre, Descripcion, Id))
    db.commit()

def borrarTarea(Id):
    cursor.execute("DELETE FROM Tareas WHERE Id= ?", (Id))
    db.commit()

def mostrarTarea():
    cursor.execute("SELECT * FROM Tareas")
    data = cursor.fetchall()
    return data

db.commit()