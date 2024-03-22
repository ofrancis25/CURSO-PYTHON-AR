import conn
import flet as ft


tareas = conn.mostrarTarea()

def main(page:ft.Page):
    global tareas
    def agregarTarea (e):
        nombre= campoNombre.value
        descripcion = campoDescripcion.value
        conn.crearTarea (nombre, descripcion)
        page.add(ft.Text(nombre))
        
    campoNombre = ft.TextField(label= "Nombre Tarea")
    campoDescripcion = ft.TextField (label= "Descripcion de la Tarea")
    botonAgregar = ft.ElevatedButton ("Agregar", on_click= agregarTarea)
    page.add (campoNombre, campoDescripcion, botonAgregar)

    for tarea in tareas:
        page.add ( ft.Text(tarea[1]))
ft.app(target=main)
