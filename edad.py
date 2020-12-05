"""Programa para calcula la edad de una persona en dias, meses y años"""
print("Programa para calcular la edad de una persona en dias meses y años.")
print("-----------------------------")
f11 = int(input("Ingrese su dia de nacimiento, en numeros "))
f12 = int(input("Ingrese su mes de nacimiento, en numeros "))
f13 = int(input("Ingrese su año de nacimiento "))
f21 = int(input("Ingrese el dia actual, en numeros "))
f22 = int(input("Ingrese el mes actual, en numeros "))
f23 = int(input("Ingrese el año actual "))
t = int(input("En que valores quiere conocer su edad recuerde que 1= Dias, 2= Meses y 3= años "))
if f21<=31 and f21>0 and f11<=31 and f11>0:
    d= f21 - f11
    if d<0:
        d=d*-1
if f22<=12 and f22>0 and f12<=12 and f12>0:
    m = f22-f12
    if m<0:
        m=m*-1
a= f23-f13

if t==1:
    r= d + (m*30)+ (a*360)
    o= "dias"
if t==2:
    r= m + (d/30)+(a*12)
    o= "meses"
if t==3:
    r= a + (m/12) + (d/360)

print ("Su resultado es",r,"",o)




