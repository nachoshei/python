import tkinter as tk
import requests

class ConversionMonedaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        self.root.geometry("300x200")

        self.label_titulo = tk.Label(root, text="Conversion de Monedas")
        self.label_titulo.pack()

        self.label_monto = tk.Label(root, text="Monto a Convertir")
        self.label_monto.pack()
        self.entry_monto = tk.Entry(root)
        self.entry_monto.pack()

        self.label_origen = tk.Label(root, text="Moneda de Origen")
        self.label_origen.pack()
        self.combo_origen = tk.StringVar()
        self.combo_origen.set ("USD")
        self.entry_origen = tk.Entry(root, textvariable=self.combo_origen)
        self.entry_origen.pack()

        self.label_destino = tk.Label(root, text="Moneda de Destino")
        self.label_destino.pack()
        self.combo_destino = tk.StringVar()
        self.combo_destino.set ("EUR")
        self.entry_destino = tk.Entry(root, textvariable=self.combo_destino)
        self.entry_destino.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

        self.boton_convertir = tk.Button(root, text="Convertir", command=self.realizar_conversion)
        self.boton_convertir.pack()

    def realizar_conversion(self):
        monto = self.entry_monto.get()
        moneda_origen = self.combo_origen.get()
        moneda_destino = self.combo_destino.get()

        url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
        response = requests.get(url)
        data = response.json()

        if moneda_destino in data["rates"]:
            tasa_conversion = data["rates"][moneda_destino]
            monto_convertido = float(monto) * tasa_conversion
            self.label_resultado.config(text=f"{monto} {moneda_origen} = {monto_convertido:.2f} {moneda_destino}")
        else:
            self.label_resultado.config(text="Moneda de destino no valida")

#Crear ventana principal

root = tk.Tk()
app = ConversionMonedaApp(root)
root.mainloop()