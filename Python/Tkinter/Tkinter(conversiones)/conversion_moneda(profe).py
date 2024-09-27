import tkinter as tk  # Importa la librería tkinter para crear interfaces gráficas
import requests        # Importa la librería requests para realizar solicitudes HTTP

# Define una clase llamada ConversorMonedasApp que manejará la interfaz de conversión
class ConversorMonedasApp:
    def __init__(self, root):
        # Constructor de la clase, inicializa la ventana principal y los elementos gráficos

        self.root = root  # Guarda la referencia de la ventana principal (root)
        self.root.title("Conversor de Monedas")  # Establece el título de la ventana
        self.root.geometry("300x200") # Formato de programa

        # Crea un título para la aplicación en la ventana
        self.label_titulo = tk.Label(root, text="Conversión de Monedas")
        self.label_titulo.pack()  # Añade el título al diseño (pack lo muestra en la ventana)

        # Crea y posiciona una etiqueta para el campo de monto a convertir
        self.label_monto = tk.Label(root, text="Monto a Convertir:")
        self.label_monto.pack()  # Coloca la etiqueta en la ventana

        # Crea una entrada de texto para que el usuario ingrese el monto
        self.entry_monto = tk.Entry(root)
        self.entry_monto.pack()  # Añade la entrada de texto a la ventana

        # Crea y posiciona una etiqueta para la moneda de origen
        self.label_origen = tk.Label(root, text="Moneda de Origen:")
        self.label_origen.pack()  # Coloca la etiqueta en la ventana

        # Crea una variable para almacenar la moneda de origen y la inicializa con "USD"
        self.combo_origen = tk.StringVar()
        self.combo_origen.set("USD")  # Valor por defecto "USD" (dólares estadounidenses)

        # Crea una entrada de texto que está vinculada a la variable combo_origen
        self.entry_origen = tk.Entry(root, textvariable=self.combo_origen)
        self.entry_origen.pack()  # Añade la entrada de texto a la ventana

        # Crea y posiciona una etiqueta para la moneda de destino
        self.label_destino = tk.Label(root, text="Moneda de Destino:")
        self.label_destino.pack()  # Coloca la etiqueta en la ventana

        # Crea una variable para almacenar la moneda de destino y la inicializa con "EUR"
        self.combo_destino = tk.StringVar()
        self.combo_destino.set("EUR")  # Valor por defecto "EUR" (euros)

        # Crea una entrada de texto que está vinculada a la variable combo_destino
        self.entry_destino = tk.Entry(root, textvariable=self.combo_destino)
        self.entry_destino.pack()  # Añade la entrada de texto a la ventana

        # Crea y posiciona una etiqueta vacía donde se mostrará el resultado de la conversión
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()  # Coloca la etiqueta en la ventana

        # Crea un botón que llamará al método realizar_conversion cuando sea presionado
        self.boton_convertir = tk.Button(root, text="Convertir", command=self.realizar_conversion)
        self.boton_convertir.pack()  # Añade el botón a la ventana

    # Define el método que realizará la conversión de monedas
    def realizar_conversion(self):
        # Obtiene el valor ingresado en el campo de monto
        monto = self.entry_monto.get()

        # Obtiene la moneda de origen seleccionada
        moneda_origen = self.combo_origen.get()

        # Obtiene la moneda de destino seleccionada
        moneda_destino = self.combo_destino.get()

        # Construye la URL para hacer la solicitud a la API de tipo de cambio con la moneda de origen
        url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"

        # Realiza una solicitud GET a la API
        response = requests.get(url)

        # Convierte la respuesta de la API a formato JSON
        data = response.json()

        # Verifica si la moneda de destino está en los tipos de cambio obtenidos
        if moneda_destino in data["rates"]:
            # Obtiene la tasa de conversión de la moneda de destino
            tasa_conversion = data["rates"][moneda_destino]

            # Calcula el monto convertido multiplicando el monto por la tasa de conversión
            monto_convertido = float(monto) * tasa_conversion

            # Actualiza la etiqueta de resultado con el monto convertido
            self.label_resultado.config(text=f"{monto} {moneda_origen} = {monto_convertido:.2f} {moneda_destino}")
        else:
            # Si la moneda de destino no es válida, muestra un mensaje de error
            self.label_resultado.config(text="Moneda de destino no válida")

# Crear la ventana principal (root)
root = tk.Tk()

# Crear una instancia de la clase ConversorMonedasApp, pasando la ventana principal como argumento
app = ConversorMonedasApp(root)

# Ejecutar el bucle principal de la ventana, para que la interfaz esté en funcionamiento
root.mainloop()