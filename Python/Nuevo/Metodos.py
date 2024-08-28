#Importar las librerías necesariasAlgoritmo escuelaA
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Cargar los datos históricos
datos = pd.read_csv("datos_historicos.csv")

#Preparar los datos para el entrenamiento
X = datos.drop("target", axis=1)
y = datos["target"]

#Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Crear un modelo de regresión lineal
modelo = LinearRegression()

#Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

#Hacer predicciones con los datos de prueba
predicciones = modelo.predict(X_test)

#Evaluar la precisión del modelo
rmse = mean_squared_error(y_test, predicciones, squared=False)
print(f"Error cuadrático medio: {rmse:.2f}")