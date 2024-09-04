def cargar_tablas(tablas_multiplicar, limite_tabla):
	for indice_fila in range (limite_tabla):
		cargar_tabla_del(indice_fila + 1, limite_tabla, tablas_multiplicar )

def cargar_tabla_del(nro_tabla, limite_tabla, tablas_multiplicar):

	for indice in range(1, limite_tabla + 1):
		tablas_multiplicar[nro_tabla - 1][indice - 1] = nro_tabla * indice

def mostrar_tablas(tablas_multiplicar, limite_tabla):
	for indice_fila in range(limite_tabla):
		print(f"Tabla del {indice_fila + 1}:", end=" ")
		for indice_columna in range(limite_tabla):
			print(tablas_multiplicar[indice_fila][indice_columna], end=" ")
		print()

def tablas_de_multiplicar():
    limite_tabla = int(input("Hasta que tabla desea calcular: "))
    
    tablas_multiplicar = [[0 for _ in range(limite_tabla)] for _ in range(limite_tabla)]
    
    cargar_tablas(tablas_multiplicar, limite_tabla)
	
    mostrar_tablas(tablas_multiplicar, limite_tabla)

tablas_de_multiplicar()