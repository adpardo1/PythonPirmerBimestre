"""Programa para verifivar numeros primos hasta un limite"""
#Inicializacion y delaracion de variables
n= int(input("Ingrese el limite de números a verificar: "))
cont=1
cont1=1
divisor=0
while cont <=n:
    num= int(input("Ingrese el numero a verificar: "))
    while cont1<=num:
        if num%cont1==0:
            divisor = divisor + 1
        cont1 = cont1 + 1
    if divisor == 2 :
        print(num," es primo")
    else:
        print(num," no es primo")
    cont1=1
    divisor=0
    cont = cont +1

        
