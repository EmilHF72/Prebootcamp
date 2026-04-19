# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Emil" con el nombre en una variable
nombre = "Emil" # declaración de variable [cite: 1]
print("Hola,", nombre) # con una coma (agrega un espacio automáticamente)
print("Hola, " + nombre) # con un + (requiere espacio manual en el string)

# 3. Imprimir "Hola 13!" con el número en una variable
numero = 13 # declaración de variable. Tipo: Numeral [cite: 1]
print("Hola", numero, "!") # con una coma

# 3b. Intento de concatenación con +
# print("Hola " + numero + "!") # Esto arrojaría un TypeError 
# BONUS NINJA: Corregido con conversión (str)
print("Hola " + str(numero) + "!") 

# 4. Imprimir "Me encanta comer fideos con salsa y comida China"
comida1 = "fideos con salsa"
comida2 = "comida China"

# con .format()
print("¡Me encanta comer {} y {}!".format(comida1, comida2))

# con una cadena f (f-string)
print(f"¡Me encanta comer {comida1} y {comida2}!")

# BONUS NINJA: Otros métodos de cadena
print(nombre.upper()) # Convierte a mayúsculas: EMIL
print(comida2.replace("China", "Japonesa")) # Reemplaza texto