import tkinter as tk
import random

class JuegoAdivinaNumero:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el numero")
        self.root.geometry("300x200")

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        self.label_intrucciones = tk.Label(root, text="Estoy pensando en un numero entre 1 y 100.")
        self.label_intrucciones.pack()

        self.label_suposicion = tk.Label(root, text="Introduce tu suposicion")
        self.label_suposicion.pack()

        self.entry_suposicion = tk.Entry(root)
        self.entry_suposicion.pack()

        self.boton_verificar = tk.Button(root, text="Verificar", command=self.verificar_suposicion)
        self.boton_verificar.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def verificar_suposicion(self):
        suposicion = int(self.entry_suposicion.get())
        self.intentos += 1

        if suposicion < self.numero_secreto:
            resultado = "Demasiado bajo."
        elif suposicion > self.numero_secreto:
            resultado = "Demasiado alto."
        else:
            resultado = f"¡Correcto! ¡Adivinaste en {self.intentos} intentos!"
            self.boton_verificar.config(state="disabled")
        
        self.label_resultado.config(text=resultado)

#Crear ventana principal
root = tk.Tk()
app = JuegoAdivinaNumero(root)
root.mainloop()