lista1=[]
lista2=[]
puntaje=int(input("ingrese puntaje obtenido hoy:"))
for x in range (1,16):
    if puntaje<100 and puntaje>0:
        print("ingrese puntaje del 1 al 100.")
    if puntaje>=60 and puntaje<100:
     lista1.append(puntaje)
    elif puntaje<60 and puntaje>0:
        lista2.append(puntaje)
    if x==15:
        break
    puntaje=int(input("ingrese puntaje obtenido hoy:"))
    
print("los dias mayores o iguales a 60 puntos son:",lista1)
print("los dias menores a 60 puntos son:",lista2)
 







 


