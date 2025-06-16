# PARCIAL-III

# Funcionalidades
1. Agregar, eliminar y marcar tareas como completadas.
2. Filtrar tareas por fechas: ver todas, ver hoy o ver la semana.
3. Recordatorios de tareas próximas (hoy y mañana).
4. Visualización de tareas en una lista con colores según la prioridad.
5. Interfaz gráfica interactiva donde el usuario puede interactuar con la agenda.


# Importacion de modulos

- Tkinter: módulo para crear la interfaz gráfica.
- Messagebox: muestra cuadros de diálogo (como advertencias o mensajes).
- Ttk: widgets avanzados (como Combobox).
- Datetime y timedelta: para trabajar con fechas y horas.

# Clase "Tarea"
Sus atributos:
- Titulo: nombre de la tarea.
- Descripcion: detalle adicional.
- Fecha_hora: objeto datetime con la fecha y hora de la tarea.
- Prioridad: Alta, Media o Baja.
- Categoria: etiqueta para clasificar la tarea.
- Completada: si ya se terminó (True o False).
- def __str__(self): Este método devuelve una cadena representativa de la tarea para mostrarla en pantalla, si está completada, se le pone un "✓".

# Clase agenda
la lista completa de tareas y métodos para administrarlas:
- Agregar_tarea(tarea): añade una tarea.
- Eliminar_tarea(index): la elimina por su posición en la lista.
- Marcar_completada(index): la marca como completada.
- Obtener_tareas(filtro): devuelve tareas según el filtro: todas, hoy o semana.

# Clase "InterfazAgenda"
- root: ventana principal de Tkinter.
- nombre_usuario: se muestra en el título de la ventana.

# Entrada de datos
self.entry_titulo = tk.Entry(...) </br>
self.entry_descripcion = tk.Entry(...)</br>
self.entry_fecha = tk.Entry(...)</br>
self.entry_hora = tk.Entry(...)</br>

***Aqui son los campos de texto donde el usuario escribe la informacion de la tarea. </br>***

# Combobox de prioridad y categoría
self.combo_prioridad = ttk.Combobox(..., values=["Alta", "Media", "Baja"])</br>
self.combo_categoria = ttk.Combobox(..., values=["Trabajo", "Estudio", "Personal", "Otro"])</br>

- state="readonly": impide que el usuario escriba algo fuera de las opciones.
- width=10: ancho del campo (en caracteres aproximadamente).
- .set("Media"): la prioridad inicial será "Media".

# Lista de tareas
- self.lista_tareas = tk.Listbox(...)
  
***Muestra todas las tareas agregadas con colores y formato.***

# Botones
tk.Button(..., command=self.agregar_tarea)</br>
tk.Button(..., command=self.marcar_completada)</br>
tk.Button(..., command=self.eliminar_tarea)</br>

***Botones para agregar tareas, eliminarlas, marcarlas como completadas, cambiar el filtro, o salir.***

# Metodos importantes 
1. **agregar_tarea </br>**
Lee los campos, crea una instancia Tarea, la añade a la agenda y actualiza la lista. </br>
2. **actualizar_lista </br>**
Actualiza el Listbox según el filtro seleccionado (todas, hoy, semana). Aplica:
  - Color según prioridad
  - Fondo gris si está completada
  - mostrar_recordatorios
Muestra una ventana emergente si hay tareas próximas (hoy o mañana).

# Pantalla de bienvenida 
- def iniciar_agenda(): </br>
Esta función se ejecuta al inicio. Muestra una ventana para ingresar el nombre del usuario y luego carga la agenda.

# Ejecucion del programa
- if __name__ == "__main__": </br>
***Este bloque se ejecuta solo si corres el archivo directamente. Lanza la ventana de bienvenida, luego la agenda.***

# Personalizaciones
1 **Colores por prioridad:** </br>
-Alta = rojo</br>
-Media = naranja</br>
-Baja = verde</br>
2. **Completadas se ven en gris claro**</br>
3. **Botón de salida en rojo**</br>
  
