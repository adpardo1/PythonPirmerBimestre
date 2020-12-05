"""Programa para verificar y sumar numeros pares e impares"""
#Declaracion e inicializacion de variables
cont=1
sumapar=0
sumaimpar=0
sumaneg=0
sumapos=0
#Procesos
n=int(input("Ingrese el limite de numeros a verificar"))
while cont <=n:
    num=int(input("Ingrese el numero a verificar"))
    if num%2==0:
        sumapar =sumapar + num
    else:
        sumaimpar = sumaimpar + num
    if num>0:
        sumapos = sumapos + num
    else:
        sumaneg = sumaneg + num
    cont= cont + 1
    print("La suma de los pares es: ",sumapar)
    print("La suma de los impares es: ",sumaimpar)
    print("La suma de los positivos es: ",sumapos)
    print("La suma de los negativos es: ",sumaneg)
print("Sumas totales")
print("")
print("La suma de los pares es: ",sumapar)
print("La suma de los impares es: ",sumaimpar)
print("La suma de los positivos es: ",sumapos)
print("La suma de los negativos es: ",sumaneg)
