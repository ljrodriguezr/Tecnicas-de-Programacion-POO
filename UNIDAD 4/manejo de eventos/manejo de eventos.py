import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Debe escribir una tarea.")

# Función para marcar una tarea como completada
def mark_completed(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        if not task.startswith("[Completada]"):
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, "[Completada] " + task)
    except IndexError:
        messagebox.showwarning("Selección Error", "Debe seleccionar una tarea.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selección Error", "Debe seleccionar una tarea.")

# Función para cerrar la aplicación
def close_app(event=None):
    window.quit()

# Crear la ventana principal
window = tk.Tk()
window.title("Gestor de Tareas")

# Crear el campo de entrada para nuevas tareas
entry_task = tk.Entry(window, width=40)
entry_task.pack(pady=10)

# Asignar atajo para añadir tarea con la tecla "Enter"
entry_task.bind("<Return>", add_task)

# Crear el botón para añadir tarea
button_add_task = tk.Button(window, text="Añadir Tarea", command=add_task)
button_add_task.pack(pady=5)

# Crear la lista para mostrar las tareas
listbox_tasks = tk.Listbox(window, width=50, height=10)
listbox_tasks.pack(pady=10)

# Crear los botones de acciones
button_mark_completed = tk.Button(window, text="Marcar Completada", command=mark_completed)
button_mark_completed.pack(pady=5)

button_delete_task = tk.Button(window, text="Eliminar Tarea", command=delete_task)
button_delete_task.pack(pady=5)

# Asignar atajos de teclado
window.bind("<Escape>", close_app)  # Cerrar con "Esc"
window.bind("<c>", mark_completed)  # Marcar completada con "C"
window.bind("<Delete>", delete_task)  # Eliminar con "Delete"

# Ejecutar la aplicación
window.mainloop()

