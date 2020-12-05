"""Programa que permite encontrar la potencia de un numero"""
base=int(input("Ingrese la base de la potencia: "))
pot= int(input("Ingrese la potencia: "))
"""Procesos"""
cont=1
r=1
while cont<=pot:
    r=r * base
    cont= cont +1
print("La potencia de: ",base," elevada a ",pot,"es: ",r)
