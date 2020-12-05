"""SERIE FIBONACCI"""

n=int(input("Ingrese el limite de la seri de Fibonacci: "))
primero=0
segundo=1
i=1
print("")
while i<=n/2:
    print(i,", ",primero)
    print(i,", ",segundo)
    primero = primero + segundo
    segundo = primero + segundo
    i=i+1

