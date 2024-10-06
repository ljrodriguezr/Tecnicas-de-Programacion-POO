import tkinter as tk
from tkinter import ttk


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")  # Título de la ventana
        self.root.geometry("450x450")  # Tamaño de la ventana

        # Crear el campo de entrada de tareas en la parte superior
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=15)

        self.task_label = tk.Label(self.input_frame, text="Nueva tarea:")
        self.task_label.pack(side=tk.LEFT, padx=5)

        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir tareas
        self.add_task_btn = tk.Button(self.input_frame, text="Añadir", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT, padx=5)

        # Crear un Listbox para las tareas
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Asignar eventos de teclas para el Listbox
        self.task_listbox.bind("<Delete>", self.remove_task)  # Eliminar con Delete
        self.task_listbox.bind("<d>", self.remove_task)  # Eliminar con D
        self.task_listbox.bind("<c>", self.mark_completed)  # Completar con C
        self.root.bind("<Escape>", self.close_app)  # Salir con Escape

        # Frame para botones adicionales
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Botón de "Completar"
        self.complete_task_btn = tk.Button(self.button_frame, text="Completar", command=self.mark_completed)
        self.complete_task_btn.pack(side=tk.LEFT, padx=5)

        # Botón de "Eliminar"
        self.delete_task_btn = tk.Button(self.button_frame, text="Eliminar", command=self.remove_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, f"{task} - Pendiente")
            self.task_entry.delete(0, tk.END)

    def mark_completed(self, event=None):
        try:
            index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(index)
            if "Pendiente" in task_text:
                self.task_listbox.delete(index)
                completed_task = task_text.replace("Pendiente", "Completada")
                self.task_listbox.insert(index, completed_task)
        except IndexError:
            pass

    def remove_task(self, event=None):
        try:
            selected_task = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task)
        except IndexError:
            pass

    def close_app(self, event=None):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()