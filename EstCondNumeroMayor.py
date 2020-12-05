""" Estructuras condicionales"""
print("Programa para concer cual numero es el mayor de tres ")
n1 = float(input("Ingrese el primer numero "))
n2 = float(input("Ingrese el segundo numero "))
n3 = float(input("Ingrese el tercer numero "))

#Estructura condicional simple

if n1>n2 and n1>n3:
    print("Su numero ",n1,", es mayor")
if n2>n1 and n2>n3:
    print("Su numero ",n2,", es mayor")
if n3>n2 and n3>n1:
    print("Su numero ",n3,", es mayor")
    
#Estructura condicional compuesta

if n1>n2 and n1>n3:
    print("Su numero ",n1,", es mayor")
else:
    print("Su numero ",n1,", no es el mayor")
if n2>n1 and n2>n3:
    print("Su numero ",n2,", es mayor")
else:
    print("Su numero ",n2,", no es el mayor")
if n3>n2 and n3>n1:
    print("Su numero ",n3,", es mayor")
else:
    print("Su numero ",n3,", no es el mayor")

#Estructura condicional anidada
if n1>n2 and n1>n3:
    print("Su numero ",n1,", es mayor")
else:
    if n2>n1 and n2>n3:
        print("Su numero ",n2,", es mayor")
    else:
        if n3>n2 and n3>n1:
            print("Su numero ",n3,", es mayor")
    
    
