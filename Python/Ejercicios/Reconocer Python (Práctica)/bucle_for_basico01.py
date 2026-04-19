# ejercicio 01 Básico: imprime todos los números enteros del 0 al 100.
print("--- Ejercicio 01 ---")
for x in range(101):  
    print(x)

# ejercicio 02 Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("\n--- Ejercicio 02 ---")
for x in range(2, 501, 2): 
    print(x)

# ejercicio 03 Contando Vanilla Ice: imprime los números enteros del 1 al 100. 
# Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
print("\n--- Ejercicio 03 ---")
for x in range(1, 101):
    if x % 10 == 0: 
        print("baby")
    elif x % 5 == 0:
        print("ice ice")
    else:
        print(x)

# ejercicio 04 Wow. Número gigante a la vista: suma los números pares del 0 al 500,000
print("\n--- Ejercicio 04 ---")
suma_total = 0 
for x in range(0, 500001, 2):
    suma_total += x
print(suma_total) 

# ejercicio 05 Regrésame al 3: imprime los números positivos comenzando desde 2024 de 3 en 3.
print("\n--- Ejercicio 05 ---")
for x in range(2024, 0, -3): 
    print(x)

# ejercicio 06 Contador dinámico
print("\n--- Ejercicio 06 ---")
numInicial = 3  
numFinal = 10 
multiplo = 2  
for x in range(numInicial, numFinal + 1): 
    if x % multiplo == 0: 
        print(x)