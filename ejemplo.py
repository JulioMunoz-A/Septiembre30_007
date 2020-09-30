#ingresar dos numero como int
a= int (input("digite primer numero: "))
b= int (input("digite segundo numero:"))

#operaciones matematicas

suma=a+b
multi=a*b

#mostramos los resultados
print("Al sumar " + str (a) + " Con el numero " + str(b) + " El resultado sera: " + str(suma))
print("Al multiplicar " + str (a) + "Con el numero " + str(b) + "El resultado sera: " + str(multi))
#implementamos una condicion


if (a>b): 
    print("El numero " + str(a) + " Es mayor que " + str(b))
elif(a<b):
    print("El numero " + str(b) + " Es mayor que " + str(a))
else:
    print("Los numeros son iguales")   