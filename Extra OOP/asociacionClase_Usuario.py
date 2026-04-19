from tarjetacredito import TarjetaCredito


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        # BONUS: Diccionario para manejar múltiples tarjetas
        self.tarjetas = {} 

    def agregar_tarjeta(self, nombre_tarjeta, limite, intereses):
        # Creamos una instancia de TarjetaCredito y la guardamos en el diccionario
        self.tarjetas[nombre_tarjeta] = TarjetaCredito(limite, intereses)
        return self

    def hacer_compra(self, monto, nombre_tarjeta="principal"):
        # Accedemos al método compra de la instancia TarjetaCredito
        self.tarjetas[nombre_tarjeta].compra(monto)
        return self

    def pagar_tarjeta(self, monto, nombre_tarjeta="principal"):
        # Accedemos al método pago de la instancia TarjetaCredito
        self.tarjetas[nombre_tarjeta].pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"\nUsuario: {self.nombre}")
        for nombre, tarjeta in self.tarjetas.items():
            print(f"  Tarjeta [{nombre}] - ", end="")
            tarjeta.mostrar_info_tarjeta()
        return self

# --- PRUEBA DE FUNCIONAMIENTO ---

# 1. Creamos al usuario
pablo = Usuario("Pablo", "pablo@mail.com")

# 2. Le asignamos dos tarjetas (Asociación)
pablo.agregar_tarjeta("Visa", 50000, 0.02)
pablo.agregar_tarjeta("Mastercard", 100000, 0.01)

# 3. Realizamos operaciones especificando la tarjeta
pablo.hacer_compra(5000, "Visa").hacer_compra(10000, "Mastercard")
pablo.pagar_tarjeta(2000, "Visa")

# 4. Mostramos el resumen
pablo.mostrar_saldo_usuario()

