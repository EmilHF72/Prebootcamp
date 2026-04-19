class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"¡{self.nombre} está jugando! Felicidad +10, Salud -5.")
        return self

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"¡{self.nombre} está comiendo! Felicidad +5, Salud +10.")
        return self

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"¡{self.nombre} recibió medicina! Salud +20, Felicidad -5.")
        return self

    def mostrar_estado(self):
        print(f"Estado de {self.nombre}: Salud: {self.salud} | Felicidad: {self.felicidad}")
        