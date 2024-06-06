lista=[]
nombre=input("ingrese un nombre:") 
for x in range (7):
 lista.append(nombre)
 nombre=input("ingrese un nombre:")

lista_nueva=[]
for nombre in lista:
    nombre=nombre.lower() 
    if nombre[-1]=="a":
     lista_nueva.append(nombre)
print("la lista con nombres que terminan con a son:")
print(lista_nueva)
