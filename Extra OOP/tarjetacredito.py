class TarjetaCredito:
    # Atributo de clase para el Bonus
    todas_las_tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        # Nota: El parámetro con valor por defecto (saldo_pagar) va al final
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar
        # Registro automático de la instancia
        TarjetaCredito.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        # Aumentamos el saldo sumando el interés calculado
        self.saldo_pagar += (self.saldo_pagar * self.intereses)
        return self

    @classmethod
    def imprimir_todas_las_tarjetas(cls):
        # Método de clase para el Bonus
        print("\n--- RESUMEN DE TODAS LAS TARJETAS ---")
        for tarjeta in cls.todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

#Ejecución de las Prácticas (Encadenamiento)
#crear las 3 instancias y realizar las operaciones solicitadas en una sola línea de código

# Creación de tarjetas (limite, intereses, saldo_inicial opcional)
tarjeta1 = TarjetaCredito(15000, 0.02)
tarjeta2 = TarjetaCredito(25000, 0.05, 1000)
tarjeta3 = TarjetaCredito(5000, 0.01)

# 1. Primera tarjeta: 2 compras, 1 pago, cobrar intereses y mostrar info
print("Tarjeta 1:")
tarjeta1.compra(5000).compra(3000).pago(2000).cobrar_interes().mostrar_info_tarjeta()

# 2. Segunda tarjeta: 3 compras, 2 pagos, cobrar intereses y mostrar info
print("\nTarjeta 2:")
tarjeta2.compra(5000).compra(2000).compra(3000).pago(1000).pago(500).cobrar_interes().mostrar_info_tarjeta()

# 3. Tercera tarjeta: 5 compras que excedan el límite y mostrar info
print("\nTarjeta 3:")
tarjeta3.compra(1000).compra(1000).compra(1000).compra(1000).compra(2000).mostrar_info_tarjeta()

# BONUS: Imprimir información de todas las instancias creadas
TarjetaCredito.imprimir_todas_las_tarjetas()