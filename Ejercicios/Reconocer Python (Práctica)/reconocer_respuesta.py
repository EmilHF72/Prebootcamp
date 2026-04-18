numero1 = 70 # declaración de variable, Tipos de Datos: Primitivos - Numerales
numero2 = 3.14 # declaración de variable, Tipos de Datos: Primitivos - Numerales
booleano = False # declaración de variable, Tipos de Datos: Primitivos - Boolean
cadena = 'Hola Mundo' # declaración de variable, Tipos de Datos: Primitivos - Strings (Cadenas)
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # declaración de variable, Tipos de Datos: Compuestos - Listas (inicialización)
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # declaración de variable, Tipos de Datos: Compuestos - Diccionarios (inicialización)
frutas = ('guayaba', 'fresa', 'papaya') # declaración de variable, Tipos de Datos: Compuestos - Tuplas (inicialización)
print(type(frutas)) # revisión de tipo
print(ingredientes_pastel[2]) # Listas: accesar valor
ingredientes_pastel.append('Mantequilla') # Listas: agregar valor
print(persona['nombre']) # Diccionarios: accesar valor
persona['nombre'] = 'Kevin' # Diccionarios: cambiar valor
persona['color_ojos'] = 'cafe' # Diccionarios: agregar valor
print(frutas[2]) # Tuplas: accesar valor

if numero1 > 45: # condicional - if
    print("Numero mayor")
else: # condicional - else
    print("Numero menor")

if len(cadena) < 5: # revisión de tamaño, condicional - if
    print("Cadena corta")
elif len(cadena) > 15: # revisión de tamaño, condicional - else if (elif)
    print("Cadena larga")
else: # condicional - else
    print("Cadena perfecta")

for x in range(8): # bucle for - inicio, fin
    print(x)
for x in range(2,8): # bucle for - inicio, fin
    print(x)
for x in range(2,8,2): # bucle for - inicio, fin, incremento
    print(x)
x = 0 # declaración de variable
while(x < 8): # bucle while - inicio, fin
    print(x)
    x += 1 # bucle while - incremento

ingredientes_pastel.pop() # Listas: borrar valor (último)
ingredientes_pastel.pop(1) # Listas: borrar valor (índice 1)

print(persona)
persona.pop('color_ojos') # Diccionarios: borrar valor
print(persona)

for ingrediente in ingredientes_pastel: # bucle for
    if ingrediente == 'Harina':
        continue # bucle for - continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break # bucle for - break

def imprime_hola_10_veces(): # función
    for numero in range(10): # bucle for - inicio, fin
        print('Hola')

imprime_hola_10_veces() # llamada a función

def imprime_hola_n_veces(n): # función, parámetro
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5) # función, argumento

def imprime_hola_n_o_diez_veces(n = 10): # función, parámetro por defecto
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces() # función
imprime_hola_n_o_diez_veces(5) # función, argumento


"""
Sección BONUS
comentario - múltiples líneas
"""

# print(numero3) # Bonus: NameError: name <variable name> is not defined
# numero3 = 86
# frutas[0] = 'naranja' # Bonus: TypeError: 'tuple' object does not support item assignment
# print(persona['hobbies']) # Bonus: KeyError: 'altura' (o similar por llave inexistente)
# print(ingredientes_pastel[11]) # Bonus: IndexError: list index out of range
#   print(booleano) # Bonus: IndentationError: unexpected indent
# frutas.append('manzana') # Bonus: AttributeError: 'tuple' object has no attribute 'append'
# frutas.pop(1) # Bonus: AttributeError: 'tuple' object has no attribute 'pop'