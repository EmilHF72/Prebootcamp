class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        # El saldo a pagar aumenta con cada compra
        self.saldo_pagar += monto
        return self
    
    def pagar_tarjeta(self, monto):
        # El saldo a pagar disminuye al realizar un pago
        self.saldo_pagar -= monto
        return self

    def mostrar_saldo_usuario(self):
        # Imprime nombre completo y saldo actual
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def transferir_deuda(self, otro_usuario, monto):
        # BONUS: Reduce mi deuda y se la pasa a otro
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto
        return self


# --- CREACIÓN DE INSTANCIAS ---

usuario1 = Usuario("Nariyoshi", "Miyagi", "miyagi@dojo.com")
usuario2 = Usuario("Daniel", "LaRusso", "daniel@auto.com")
usuario3 = Usuario("Johnny", "Lawrence", "johnny@cobra.com")

# --- ACCIONES ---

# 1. Primer usuario: 2 compras, 1 pago, mostrar saldo
usuario1.hacer_compra(5000)
usuario1.hacer_compra(2500)
usuario1.pagar_tarjeta(3000)
usuario1.mostrar_saldo_usuario()

# con metodos encadenados
usuario1.hacer_compra(5000).hacer_compra(2500).pagar_tarjeta(3000).mostrar_saldo_usuario()

# 2. Segundo usuario: 1 compra, 2 pagos, mostrar saldo
usuario2.hacer_compra(10000)
usuario2.pagar_tarjeta(2000)
usuario2.pagar_tarjeta(1500)
usuario2.mostrar_saldo_usuario()
# con metodos encadenados
usuario2.hacer_compra(10000).pagar_tarjeta(2000).pagar_tarjeta(1500).mostrar_saldo_usuario()

# 3. Tercer usuario: 3 compras, 4 pagos, mostrar saldo
usuario3.hacer_compra(1000)
usuario3.hacer_compra(2000)
usuario3.hacer_compra(3000)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(2000)
usuario3.mostrar_saldo_usuario()
# con metodos encadenados
usuario3.hacer_compra(1000).hacer_compra(2000).hacer_compra(3000).pagar_tarjeta(500).pagar_tarjeta(500).pagar_tarjeta(1000).pagar_tarjeta(2000).mostrar_saldo_usuario() 

# --- PRUEBA DEL BONUS (Opcional) ---
print("\n--- Probando transferencia de deuda ---")
usuario1.transferir_deuda(usuario3, 1000)
usuario1.mostrar_saldo_usuario()
usuario3.mostrar_saldo_usuario()