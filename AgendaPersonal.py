import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta


# ---------------- CLASE TAREA ----------------
class Tarea:
    def __init__(self, titulo, descripcion, fecha_hora, prioridad, categoria):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_hora = fecha_hora
        self.prioridad = prioridad
        self.categoria = categoria
        self.completada = False

    def __str__(self):
        estado = "✓ " if self.completada else ""
        fecha_str = self.fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"{estado}[{fecha_str}] {self.titulo} - {self.descripcion} ({self.categoria}, {self.prioridad})"


# ---------------- CLASE AGENDA ----------------
class Agenda:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            del self.tareas[index]

    def marcar_completada(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].completada = True

    def obtener_tareas(self, filtro="todas"):
        ahora = datetime.now()
        if filtro == "hoy":
            return [t for t in self.tareas if t.fecha_hora.date() == ahora.date()]
        elif filtro == "semana":
            fin_semana = ahora + timedelta(days=7)
            return [t for t in self.tareas if ahora.date() <= t.fecha_hora.date() <= fin_semana.date()]
        return self.tareas


# ---------------- INTERFAZ GRAFICA ----------------
class InterfazAgenda:
    def __init__(self, root, nombre_usuario):
        self.agenda = Agenda()
        self.root = root
        self.root.title(f"Agenda personal de {nombre_usuario}")

        # Título
        tk.Label(root, text="Título:").grid(row=0, column=0)
        self.entry_titulo = tk.Entry(root, width=40)
        self.entry_titulo.grid(row=0, column=1, columnspan=2)

        # Descripción
        tk.Label(root, text="Descripción:").grid(row=1, column=0)
        self.entry_descripcion = tk.Entry(root, width=40)
        self.entry_descripcion.grid(row=1, column=1, columnspan=2)

        # Fecha manual
        tk.Label(root, text="Fecha (dd/mm/yyyy):").grid(row=2, column=0)
        self.entry_fecha = tk.Entry(root, width=15)
        self.entry_fecha.grid(row=2, column=1)

        # Hora manual
        tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=2)
        self.entry_hora = tk.Entry(root, width=10)
        self.entry_hora.grid(row=2, column=3)

        # Prioridad
        tk.Label(root, text="Prioridad:").grid(row=3, column=0)
        self.combo_prioridad = ttk.Combobox(root, values=["Alta", "Media", "Baja"], state="readonly", width=10)
        self.combo_prioridad.grid(row=3, column=1)
        self.combo_prioridad.set("Media")

        # Categoría
        tk.Label(root, text="Categoría:").grid(row=3, column=2)
        self.combo_categoria = ttk.Combobox(root, values=["Trabajo", "Estudio", "Personal", "Otro"], state="readonly", width=15)
        self.combo_categoria.grid(row=3, column=3)
        self.combo_categoria.set("Personal")

        # Botón agregar
        tk.Button(root, text="Agregar tarea", command=self.agregar_tarea).grid(row=4, column=0, columnspan=4, pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, width=100, height=10)
        self.lista_tareas.grid(row=5, column=0, columnspan=4)

        # Botones acciones
        tk.Button(root, text="Marcar como completada", command=self.marcar_completada).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).grid(row=6, column=1)
        tk.Button(root, text="Ver todas", command=lambda: self.actualizar_lista("todas")).grid(row=6, column=2)
        tk.Button(root, text="Ver hoy", command=lambda: self.actualizar_lista("hoy")).grid(row=6, column=3)
        tk.Button(root, text="Ver semana", command=lambda: self.actualizar_lista("semana")).grid(row=7, column=0, pady=5)
        tk.Button(root, text="Salir", command=self.root.quit, bg="red", fg="white").grid(row=7, column=3)

        self.actualizar_lista()
        self.mostrar_recordatorios()

    def agregar_tarea(self):
        titulo = self.entry_titulo.get()
        descripcion = self.entry_descripcion.get()
        fecha_str = self.entry_fecha.get()
        hora_str = self.entry_hora.get()
        prioridad = self.combo_prioridad.get()
        categoria = self.combo_categoria.get()

        if not titulo or not fecha_str or not hora_str:
            messagebox.showerror("Error", "Título, fecha y hora son obligatorios")
            return

        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            hora = datetime.strptime(hora_str, "%H:%M").time()
            fecha_hora = datetime.combine(fecha, hora)
        except ValueError:
            messagebox.showerror("Formato incorrecto", "Usa formato fecha: dd/mm/yyyy y hora: HH:MM")
            return

        tarea = Tarea(titulo, descripcion, fecha_hora, prioridad, categoria)
        self.agenda.agregar_tarea(tarea)
        self.actualizar_lista()

        self.entry_titulo.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.agenda.eliminar_tarea(seleccion[0])
            self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.agenda.marcar_completada(seleccion[0])
            self.actualizar_lista()

    def actualizar_lista(self, filtro="todas"):
        self.lista_tareas.delete(0, tk.END)
        tareas = self.agenda.obtener_tareas(filtro)
        for tarea in tareas:
            color = "black"
            if tarea.prioridad == "Alta":
                color = "red"
            elif tarea.prioridad == "Media":
                color = "orange"
            elif tarea.prioridad == "Baja":
                color = "green"

            self.lista_tareas.insert(tk.END, str(tarea))
            self.lista_tareas.itemconfig(tk.END, {'fg': color})
            if tarea.completada:
                self.lista_tareas.itemconfig(tk.END, {'bg': "#e0e0e0"})

    def mostrar_recordatorios(self):
        hoy = datetime.now().date()
        mañana = hoy + timedelta(days=1)
        proximas = [t for t in self.agenda.obtener_tareas() if hoy <= t.fecha_hora.date() <= mañana]
        if proximas:
            mensaje = "\n".join(str(t) for t in proximas)
            messagebox.showinfo("Tareas próximas", f"Tienes tareas pendientes para hoy o mañana:\n\n{mensaje}")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    def iniciar_agenda():
        nombre = entry_nombre.get()
        if not nombre.strip():
            messagebox.showerror("Error", "Por favor, ingresa tu nombre.")
            return
        inicio.destroy()
        root = tk.Tk()
        app = InterfazAgenda(root, nombre)
        root.mainloop()

    inicio = tk.Tk()
    inicio.title("Bienvenido")
    tk.Label(inicio, text="Ingrese su nombre:").pack(padx=10, pady=5)
    entry_nombre = tk.Entry(inicio)
    entry_nombre.pack(padx=10, pady=5)
    tk.Button(inicio, text="Continuar", command=iniciar_agenda).pack(pady=10)
    inicio.mainloop()
