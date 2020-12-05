"""PROGRAMA PARA GENRAR LA SERIE 1/2 - 2/3 + 3/5 - 4/7 + 5/11 - 6/13 + … + n"""
print("PROGRAMA PARA GENRAR LA SERIE 1/2 - 2/3 + 3/5 - 4/7 + 5/11 - 6/13 + … + n")
print("")
n= int(input("Ingrese el limite de la serie: "))
primo=2
divisor=0
num=0
den=0
suma=0
n=n+1

for i in range (1,n):
    num = num +1
    bandera = True
    while bandera==True:
        for j in range (1, primo+1):
            if primo%j==0:
                divisor= divisor+1
         
        if divisor==2:
            bandera=False
            den=primo
            primo=primo+1
        else:
            primo = primo+1
            
        divisor=0
    if i%2==0:
        print(i,". -",num,"/",den)
        suma=suma - (num/den)
    else:
        print(i,". +",num,"/",den)
        suma=suma + (num/den)

print("")
print("La suma de la serie es: ",suma)
