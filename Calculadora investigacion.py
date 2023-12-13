import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def limpiar():
    entrada.delete(0, tk.END)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear la entrada
entrada = tk.Entry(ventana, width=30, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir los botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Agregar botones a la ventana
for (texto, fila, columna) in botones:
    if texto == "C":
        boton = tk.Button(ventana, text=texto, width=5, command=limpiar)
    elif texto == "=":
        boton = tk.Button(ventana, text=texto, width=5, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, width=5, command=lambda t=texto: agregar_caracter(t))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()
