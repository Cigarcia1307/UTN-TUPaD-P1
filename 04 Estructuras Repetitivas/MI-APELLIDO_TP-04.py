
#ejercicio1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for num in range (0,101):
    print(num)


#ejercicio2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num= int(input("Por favor ingrese un numero entero:"))
print (f"Usted ingreso el numero: {num}")
#contamos cantidad de digitos
cantidad_digitos= len(str(abs(num)))
print(f"El numero tiene {cantidad_digitos} digitos")

#Ejercicio3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num_uno= int(input("Por favor ingrese un numero:"))
num_dos= int(input("Por favor ingrese un numero:"))

#el primero debe ser menor que el segundo, en caso contrario invertirlos.
if num_uno>num_dos:
    num_uno,num_dos=num_dos,num_uno

#Sumamos y excluimos los que fueron ingresados
suma_numeros= sum(range(num_uno +1, num_dos))
print(f"La suma se los numeros comprendidos entre {num_uno} y {num_dos} es: {suma_numeros}")

#Ejercicio4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

acu=0
sumatoria=1

print("Ingrese un numero entero")
numero=int(input())
while sumatoria and numero !=0:
    acu+=numero
    sumatoria+=1
    print("Ingrese otro numero entero:")
    numero=int(input())
#si el usuario ingresa 0 muestra la suma de los numeros ingresados
if numero == 0:
    acu +=numero
print ("La suma de los numeros ingresados es:",acu)


#Ejercicio5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_correcto=4
acu=0

print("Ingrese un numero entero")
numero=int(input())
while numero != numero_correcto:
    acu+=1
    print("Ingrese otro numero:")
    numero=int(input())

acu += 1
print ("La cantidad de intentos fue:",acu)

#Ejercicio6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

for num in range (100,-2,-2):
    print(num)


#Ejercicio7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

sumatoria=0

print("Ingrese un numero:")
numero=int(input())
while numero >0:
    sumatoria+=numero
    numero-=1
print(f"La suma de los numeros comprendidos entre el 0 y el numero {numero} es:", sumatoria)

#Ejercicio8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impares=0
negativos=0
positivos=0

for numeros in range (100):
    print("Ingrese un numero:")
    numero=int(input())
 #determinar pares, impares
    if numero % 2==0:
        pares+=1
    else:
        impares+=1
#determinar positivos y negativos
    if numero <-0:
        negativos+=1
    elif numero>0:    
        positivos+=1

print(f"La cantidad de numeros pares es:",pares)
print(f"La cantidad de numeros impares es:",impares)  
print(f"La cantidad de numeros negativos son:",negativos)
print(f"La cantidad de numeros positivos son:",positivos)   

#Ejercicio9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
suma=0

print("Por favor ingrese numeros:")
for num in range(100):
    numero=float(input(f"Ingrese el numero {num+1}:"))
    suma+=numero

media= suma/5

print(f"La media del total de los  numeros ingresados es:", media)

#ejercicio10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero=int(input("Ingrese un numero:"))
numero_invertido = int(str(abs(numero))[::-1]) * (-1 if numero < 0 else 1)
print(f"El número invertido es: {numero_invertido}")