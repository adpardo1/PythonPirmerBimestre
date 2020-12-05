"""Transformar de metros a centimetros, kilometros, pies y pulgadas"""
print("Programa para transformar de metros a centimetros, kilometros, pies y pulgadas")
print("------------------------------------------------------------------------------")
vm=float(input("Ingrese el valor en metros: "))
vc= vm*100
vk=vm/1000
vpi= vm/3.281
vpul=vm*39.37
print("Su valor en centimetros es: ",vc)
print("Su valor en kilometros es: ",vk)
print("Su valor en pies es: ",vpi)
print("Su valor en pulgadas es: ",vpul)

