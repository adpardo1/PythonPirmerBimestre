"""Programa para ocnertir grados"""
print("Programa para convertir de grados centigrados a Kelvin y Farenheit")
gc = float(input("Ingrese su valor en grados centigrados: "))
if gc>0:
    gf =(gc*9/5)+32
    gk = (gc + 273.15)
    print("La equivalencia en grados Farenheit es: ",gf)
    print("La equivalencia en grados Kelvin es: ",gk)
