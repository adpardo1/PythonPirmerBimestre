"""Calculadora basica"""
print("Calculadora basica")
print("--------------------")
n1 = float(input("Ingrese el primer valor: "))
n2 = float(input("Ingrese el segundo valor: "))
print("1. Suma")
print("2. Resta")
print("3.Multiplicacion")
print("4. Division")
t = int(input("Ingrese una opcion: "))
if t==1:
    r= n1+n2
    print("La suma es: ",r)
if t==2:
    r= n1-n2
    print("La resta es: ",r)
if t==3:
    r = n1*n2
    print("La multiplicacion es: ",r)
if t==4:
    r= n1/n2
    print("La division es: ",r)
