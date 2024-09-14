import tkinter as tk
from tkinter import messagebox
# crear un ventana
app = tk.Tk()
app.geometry('400x500')
app.title('Tecnicas de INTERFAZ')


app.configure(background='violet')
#variables
entrada = tk.StringVar(app)
lista_datos = []

# funcion de agregar datos
def agregar_datos():
    texto_ingresado = entrada.get()
    if texto_ingresado:
        lista.insert(tk.END, texto_ingresado)
        entrada.set("")
    else:
        print("campo vacio")
# Función para limpiar la lista y el campo de entrada
def limpiar():
    lista.delete(0, tk.END)

#componentes
tk.Label(app, text="Ingrese el valor : ", font=('Lucida',12)).pack(pady=10)
tk.Entry(app, fg='blue', bg='white',font=('Lucida',10),textvariable=entrada).pack(pady=10)
tk.Button(app, text="agregar",font=('Lucida',10),bg='violet', fg='yellow', command=agregar_datos).pack(pady=10)
#lista para agregar datos
lista = tk.Listbox(app, font=('Lucida',10), width=50, height=15)
lista.pack(pady=10)
# Botón "Limpiar"
boton_limpiar = tk.Button(app, text="Limpiar", font=('Lucida', 10), bg='red', fg='white', command=limpiar)
boton_limpiar.pack(pady=10)

app.mainloop()