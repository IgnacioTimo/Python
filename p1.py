import tkinter as tk

# Creo una ventana
ventana = tk.Tk()

# Defino el título de la ventana
ventana.title("Proyecto 1")

# Defino las dimensiones de la ventana
ventana.geometry("800x600")

# Defino un texto dentro de la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo, este va a ser mi proyecto!")
etiqueta.pack()

# Mostrar la ventana
ventana.mainloop()