cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}]

def iterarDiccionario(lista):
    for diccionario in lista:
        linea = []
        for llave, valor in diccionario.items():
            linea.append("%s - %s" % (llave,valor))
        print(", ".join(linea))

iterarDiccionario(cantantes)