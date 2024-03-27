#

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento /100)
    return descuento


compra_1 = 150
descuento_1 = calcular_descuento(compra_1)
monto_final_1 = compra_1 - descuento_1
print(f"Monto del descuento: {descuento_1}")
print(f"Monto final a pagar despues del descuento: {monto_final_1}")

compra_2 = 1020
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(compra_2, porcentaje_descuento_2)
monto_final_2 = compra_2 - descuento_2
print(f"Monto del descuento: {descuento_2}")
print(f"Monto final a pagar despues del descuento: {monto_final_2}")