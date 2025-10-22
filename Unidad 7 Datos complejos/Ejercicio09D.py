# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo

agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Lunes", "14:30"): "Clase de Python",
    ("Martes", "11:00"): "Llamada con el cliente X",
    ("Miércoles", "10:00"): "Desarrollo de proyecto A",
    ("Miércoles", "17:00"): "Gimnasio",
    ("Jueves", "09:30"): "Revisión de código",
    ("Viernes", "15:00"): "Entrega de la tarea Y"
}

# Ejemplo de cómo acceder a un evento específico
evento_lunes_9am = agenda.get(("Lunes", "09:00"))
print(f"El evento del Lunes a las 09:00 es: {evento_lunes_9am}")

# Ejemplo de cómo añadir un nuevo evento
agenda[("Viernes", "11:00")] = "Preparación de la presentación"
print("\nAgenda actualizada con nuevo evento:")
print(agenda)