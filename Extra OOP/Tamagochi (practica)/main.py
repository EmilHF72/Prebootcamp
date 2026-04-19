from persona import Persona
from tamagotchi import Tamagotchi

# 1. Crear la instancia del Tamagotchi
mi_mascota = Tamagotchi("Mametchi", "Amarillo")

# 2. Crear la instancia de Persona y asignarle la mascota
dueño = Persona("Alex", "Webber", mi_mascota)

# 3. Acciones (usando encadenamiento)
dueño.darle_comida().curarlo().jugar_con_tamagotchi()

# 4. Ver el resultado final en la mascota
mi_mascota.mostrar_estado()
