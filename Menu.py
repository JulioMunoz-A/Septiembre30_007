import os
def Numeros():
    print("**** Opción de Números ****")
    #ingresar n números, donde n es un número ingresado por teclado, calcular y mostrar: 
    #cantidad de números positivos, cantidad de números negativos, y cantidad de iguales a cero

    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
    veces= int(input("Cuantos números desea ingresar?: "))
    for x in range(veces): 
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1

        print("Cantidad de números positivos: " + str(pos) +
            "\n Cantidad de números negativos : " + str(neg) + 
            "\n Cantidad de números iguales a cero: " + str(cero))    

    Pausa=input("Presiones una tecla para continuar")

def Datos():
    print("**** Opción de Datos de Personas ****")

    #ingresar para n personas donde n es un número ingresado por teclado: nombre y edad. 
    #calcular y mostrar: cantidad de personas mayores de edad y cantidad de menores de edad. 
    #subir la modificacion de github con el siguiente mensaje: "se programo la opción 2 del menú"

    
    pos=0
    neg=0
  
    veces= int(input("Cuantas personas desea ingresar?: "))
    for x in range(veces): 
        nombre=str(input("Ingrese nombre: "))
        edad=int(input("Ingrese la edad: "))
        if (edad>18):
            pos=pos+1
        elif(edad<18):
            neg=neg+1


        print("Cantidad de personas mayores de edad: " + str(pos)+ 
            "\n Cantidad de personas mayores de edad : "+ str(neg))
       

        Pausa=input("Presiones una tecla para continuar")

seguir=True
while (seguir):
    os.system('cls')
    print("1. Opción Numeros ")
    print("2. Opción Datos de Personas  ")
    print("3. Finalizar ")
    op=int(input("Ingrese opción 1, 2, 3: "))
    if (op==1):
        Numeros()
    if (op==2):
        Datos()
    if (op==3):
        seguir=False
        break

   