print("Buen día")
valor_compra = int(input("Cual fue el costo total de la compra"))

descuento_compra = 0
if valor_compra < 100:
    descuento_compra = valor_compra * 0.05

elif 100 <= valor_compra < 200:
    descuento_compra = valor_compra * 0.1

else:
    descuento_compra = valor_compra * 0.15

valor_final = valor_compra - descuento_compra

print(" El descuento total de compra fue de ", descuento_compra)
print(" El precio a pagar despues del descuento es de ", valor_final)

