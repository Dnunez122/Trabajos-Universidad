import datetime

# Obtener la fecha y hora actual del sistema
fecha_hora_actual = datetime.datetime.now()

# Formatear la fecha y hora en una cadena legible
fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Imprimir la fecha y hora formateada
print("Fecha y hora actual del sistema:", fecha_hora_formateada)
