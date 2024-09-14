import tkinter as tk
from tkinter import messagebox

# Crear una ventana
app = tk.Tk()
app.geometry('400x500')
app.title('Técnicas de INTERFAZ')

app.configure(background='violet')

# Función para agregar elementos a la lista
def agregar_elemento():
    valor = entry.get()
    if valor:
        lista.insert(tk.END, valor)
        entry.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar la lista o el campo de entrada
def limpiar():
    if lista.curselection():
        # Eliminar el elemento seleccionado de la lista
        lista.delete(tk.ANCHOR)
    else:
        # Limpiar el campo de entrada si no hay selección en la lista
        entry.delete(0, tk.END)

# Componentes
tk.Label(app, text="Ingrese el valor:", font=('Lucida', 12)).pack(pady=10)
entry = tk.Entry(app, fg='blue', bg='white', font=('Lucida', 10))
entry.pack(pady=10)

tk.Button(app, text="Agregar", font=('Lucida', 10), bg='violet', fg='yellow', command=agregar_elemento).pack(pady=10)

# Lista para agregar datos
lista = tk.Listbox(app, font=('Lucida', 10), width=50, height=10)
lista.pack(pady=10)



# Ejecutar la aplicación
app.mainloop()
