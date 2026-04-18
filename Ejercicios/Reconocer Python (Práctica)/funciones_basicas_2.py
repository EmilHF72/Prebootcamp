# funciones_basicas_2.py

# 1. Multiplica por 2
def multiplica_por_dos(num):
    # Crea una lista con los números del 0 al num multiplicados por 2
    nueva_lista = []
    for i in range(num + 1):
        nueva_lista.append(i * 2) # Concepto: manipulación de listas - append
    return nueva_lista # Concepto: return (devuelve el valor al finalizar)

# 2. Suma y resta
def suma_y_resta(lista):
    # Imprime la suma de los dos elementos
    print(lista[0] + lista[1]) # Concepto: tipos de datos compuestos - listas
    # Regresa la resta de los dos números
    return lista[0] - lista[1]

# 3. Sumatoria menos longitud
def sumatoria_menos_longitud(lista):
    sumatoria = 0
    # Recorremos la lista para sumar sus elementos
    for valor in lista:
        sumatoria += valor
    # Regresa la suma total menos el tamaño de la lista
    return sumatoria - len(lista) # len() se usa para la revisión de tamaño

# 4. Valores multiplicados por el segundo
def valores_multiplicados_segundo(lista):
    # Imprimimos la longitud primero
    print(len(lista))
    
    # Validación: si la lista tiene menos de 2 elementos
    if len(lista) < 2:
        return [] # Regresa lista vacía
        
    segundo_valor = lista[1]
    nueva_lista = []
    # Creamos la nueva lista multiplicando cada valor por el segundo elemento
    for valor in lista:
        nueva_lista.append(valor * segundo_valor)
    return nueva_lista

# 5. Valor multiplicado y longitud
def valor_multiplicado_longitud(valor, longitud):
    # El valor a repetir es longitud * valor
    resultado_multiplicacion = longitud * valor
    nueva_lista = []
    # El bucle se repite tantas veces como indique 'longitud'
    for i in range(longitud):
        nueva_lista.append(resultado_multiplicacion)
    return nueva_lista

# --- Pruebas de los ejercicios ---
print("Ej 1:", multiplica_por_dos(5))
print("Ej 2 (Resta):", suma_y_resta([5, 4]))
print("Ej 3:", sumatoria_menos_longitud([1, 2, 3, 4]))
print("Ej 4:", valores_multiplicados_segundo([1, 3, 5, 7]))
print("Ej 5:", valor_multiplicado_longitud(7, 5))