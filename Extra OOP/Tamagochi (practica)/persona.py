from tamagotchi import Tamagotchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        # Aquí ocurre la asociación: el atributo es una instancia de otra clase
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} saca los juguetes...")
        self.tamagotchi.jugar()
        return self

    def darle_comida(self):
        print(f"{self.nombre} prepara un bocadillo...")
        self.tamagotchi.comer()
        return self

    def curarlo(self):
        print(f"{self.nombre} nota a su mascota enferma...")
        self.tamagotchi.curar()
        return self