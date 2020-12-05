"""Programa para convertir un reloj de 24 horas a 12 horas"""
print("Programa para convertir el formato de 24 horas a 12 horas")
h24 = int(input("Ingrese la hora en formato de 24 horas a transformar "))
m24 = int(input("Ingrese los minutos a transformar "))
if h24<25 and h24 >= 0:
    if h24 >= 0 and h24<=24 and m24 >=0 and m24<=60:
        if m24 == 60 and h24<24:
            h24 = h24 + 1
            m24 = 0
            h12 = h24 - 12
            m12 = m24
        else:
            m12 = m24
        if h24 >= 12:
            h12 = h24 -12
            periodo = "p.m."
              
        else:
            h12 = h24
            periodo ="a.m."                 
        if h24 == 0:
            h12= 12
            periodo ="a.m."
            if h24 == 24 and m24 == 60:
                h12=12
                m12=0
                periodo = "a.m."
        print("El tiempo de ",h24," horas y ",m24," minutos")
        print("Equivalente a ",h12," horas y ",m12," minutos "+periodo)
                              
                              
        
    
else:
    print("Error: el valor ingresado no debe superar las 24 horas")
