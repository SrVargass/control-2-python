lista=[]
valor = input("Ingresar nombre (No escriba nada y presione Enter para finalizar): ")

while valor != "":
    lista.append(valor)
    valor = input("Ingresar nombre (No escriba nada y presione Enter para finalizar): ")
if len(lista)==0:
    print("no se ingresaron datos")
else:
 pala=""
 caracteres=0
 for palabra in lista:
      if (len(palabra))>caracteres:
          pala=palabra
          caracteres=len(palabra)
print("La palabra con mayor cantidad de caracteres es:", pala)
print("La cantidad de caracteres de la palabra es:", caracteres)
