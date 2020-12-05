"""Programa para calcular el area de un terreno"""
print("Programa para calcular el area y costo de un terreno")
print("-----------------------------------------------------")
va = float(input("Ingrese el valor de A en metros: "))
vb = float(input("Ingrese el valor de B en metros: "))
vc = float(input("Ingrese el valor de C en metros: "))
costo = float(input("Ingrese el costo por metros: "))

at= va-vc
art=(vb*at)/2
arr= vb*vc
area= art + arr
total= costo * area
print("El area del terreno es: ",area,", con un valor total de ",total,", dolares")
print("Compuesto de un triangulo de area ",arr," y un rectangulo de area ",art)
