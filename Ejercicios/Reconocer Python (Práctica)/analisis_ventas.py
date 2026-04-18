# 1. Carga de Datos
# Una lista de diccionarios que representa las ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Teclado", "cantidad": 10, "precio": 25.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 15.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 2, "precio": 30.0},
    {"fecha": "2024-01-02", "producto": "Monitor", "cantidad": 3, "precio": 150.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 8, "precio": 12.0}
]

# 2. Cálculo de Ingresos Totales
ingresos_totales_globales = 0
for venta in ventas:
    # Ingreso por venta = cantidad * precio unitario
    ingresos_totales_globales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    if prod not in ventas_por_producto:
        ventas_por_producto[prod] = 0
    ventas_por_producto[prod] += venta["cantidad"]

# Identificar el más vendido
producto_mas_vendido = ""
max_cantidad = 0
for prod, cant in ventas_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        producto_mas_vendido = prod

# 4. Promedio de Precio por Producto (Usando Tuplas)
# Formato: { "producto": (suma_precios, cantidad_total) }
precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    if prod not in precios_por_producto:
        precios_por_producto[prod] = (0, 0)
    
    # Actualizamos la tupla acumulando (ingreso, cantidad)
    actual_ingreso, actual_cantidad = precios_por_producto[prod]
    precios_por_producto[prod] = (actual_ingreso + ingreso_venta, actual_cantidad + venta["cantidad"])

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    dia = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if dia not in ingresos_por_dia:
        ingresos_por_dia[dia] = 0
    ingresos_por_dia[dia] += ingreso

# 6. Representación de Datos
resumen_ventas = {}
for prod in ventas_por_producto:
    ingreso_acum, cant_acum = precios_por_producto[prod]
    resumen_ventas[prod] = {
        "cantidad_total": cant_acum,
        "ingresos_totales": ingreso_acum,
        "precio_promedio": ingreso_acum / cant_acum if cant_acum > 0 else 0
    }

# --- IMPRESIÓN DE RESULTADOS PARA GOOGLE SHEETS ---
print(f"INGRESOS TOTALES: {ingresos_totales_globales}\n")
print(f"PRODUCTO MÁS VENDIDO: {producto_mas_vendido} ({max_cantidad} unidades)\n")

print("PRECIO PROMEDIO POR PRODUCTO:")
for prod, info in resumen_ventas.items():
    print(f"{prod}: {info['precio_promedio']}")

print("\nINGRESOS POR DÍA:")
for dia, monto in ingresos_por_dia.items():
    print(f"{dia}: {monto}")

print("--- RESUMEN DE VENTAS POR PRODUCTO ---")
for producto, info in resumen_ventas.items():
    print(f"Producto: {producto}")
    print(f"  - Cantidad Total: {info['cantidad_total']}")
    print(f"  - Ingresos Totales: ${info['ingresos_totales']}")
    print(f"  - Precio Promedio: ${info['precio_promedio']:.2f}")
    print("-" * 30)