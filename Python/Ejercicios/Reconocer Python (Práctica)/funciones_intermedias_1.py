# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1. Cambia el valor de 3 en matriz por 6
# El '3' está en la segunda lista (índice 1) y es el primer elemento (índice 0)
matriz[1][0] = 6

# 2. Cambia "Ricky Martin" por "Enrique Martin Morales"
# Es el primer elemento de la lista (índice 0) y la llave es "nombre"
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 3. En ciudades, cambia “Cancún” por “Monterrey”
# La llave es "México" y "Cancún" es el tercer elemento de su lista (índice 2)
ciudades["México"][2] = "Monterrey"

# 4. En las coordenadas, cambia el valor de “latitud” por 9.9355431
# Es el primer diccionario de la lista (índice 0) y la llave es "latitud"
coordenadas[0]["latitud"] = 9.9355431

# Comprobación de resultadoscl
print("Matriz:", matriz)
print("Cantante:", cantantes[0]["nombre"])
print("Ciudades México:", ciudades["México"])
print("Coordenadas:", coordenadas)

#2. Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# iterarDiccionario(cantantes)
#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)
#BONUS: Que aparezcan en este formato:
#nombre - Ricky Martin, pais - Puerto Rico
#nombre - Chayanne, pais - Puerto Rico
#nombre - José José, pais - México
#nombre - Juan Luis Guerra, pais - República Dominicana

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}]

def iterarDiccionario(lista):
    # Recorremos cada diccionario dentro de la lista
    for diccionario in lista:
        linea = []
        # Recorremos cada llave y valor del diccionario
        for llave, valor in diccionario.items():
            # Creamos el formato "llave - valor"
            linea.append(f"{llave} - {valor}")
        # Unimos los elementos con una coma y espacio para el formato final
        print(", ".join(linea))

# Llamada a la función
iterarDiccionario(cantantes)

# 3. Obtener valores de una lista de diccionarios

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}]

def iterarDiccionario2(llave, lista):
    # Recorremos cada diccionario en la lista
    for diccionario in lista:
        # Usamos la llave recibida para imprimir el valor correspondiente
        # Accedemos mediante la sintaxis diccionario[llave]
        print(diccionario[llave])

# Pruebas de la función
print("--- Nombres ---")
iterarDiccionario2("nombre", cantantes)

print("\n--- Países ---")
iterarDiccionario2("pais", cantantes)

#4. Iterar a través de un diccionario con valores de lista

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    # Recorremos el diccionario obteniendo la llave y la lista asociada
    for llave, lista in diccionario.items(): # Concepto: items() para obtener llave y valor
        # Imprimimos el tamaño de la lista y la llave en mayúsculas
        # Usamos len() para la revisión de tamaño
        print(f"{len(lista)} {llave.upper()}")
        
        # Recorremos la lista para imprimir cada valor individualmente
        for valor in lista: # Concepto: bucle for para iterar listas
            print(valor)
        
        # Imprimimos una línea en blanco para separar las secciones
        print("")

# Llamada a la función
imprimirInformacion(costa_rica)