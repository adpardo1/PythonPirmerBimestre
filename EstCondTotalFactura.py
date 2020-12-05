"""Programa para conocer el valor de una factura con descuento"""
print("Programa para conocer el valor de una factura con descuento")
print("-------------------------------------------------------------")
subtotal = float(input("Ingrese el subtotal de la factura: "))
limite1 = 200
limite2 = 500
if subtotal >= limite1 and subtotal < limite2:
    descuento = 0.10
    total = subtotal - (subtotal * descuento)
    print("Su valor total a pagar es de: ",total,", con un descuento de: ",descuento)
else:
    if subtotal >= limite2:
        descuento = 0.15
        total = subtotal - (subtotal * descuento)
        print("Su valor total a pagar es de: ",total,", con un descuento de: ",descuento)
if subtotal < limite1:
    print("No hay descuento disponible para compras menores a 200$")
    print("Su valor total a pagar es de: ",subtotal)


