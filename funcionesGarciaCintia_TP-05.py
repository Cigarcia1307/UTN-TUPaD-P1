#Ejercicio1
#Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
 

def imprimir_hola_mundo ():
    print("¡Hola Mundo!")
    
# Llamar a esta función desde el programa principal
imprimir_hola_mundo()

#Ejercicio2
#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
 #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
 

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

nombre_usuario= input("Ingrese su nombre por favor:")
# Llamar a esta función desde el programa principal solicitando el nombre al usuario
print(saludar_usuario(nombre_usuario))

#Ejercicio3
#Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros
# e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 

 
def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
nombre=input ("Por favor ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("ingrese su edad:")
residencia=input("Ingrese su lugar de residencia:")

print(informacion_personal(nombre, apellido, edad,residencia))
   
    
#Ejercicio4
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del 
# círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi* radio

#Solicitar el radio al usuario l
radio=float(input("Ingrese el radio del circulo:"))

#llamar ambas funciones para mostrar los resultados.
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")
    
#Ejercicio5
#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y 
# devuelva la cantidad de horas correspondientes.



def segundos_a_horas(segundos):
    return segundos / 3600

#Solicitar al usuario los segundos y mostrar el resultado usando esta función.
segundos= float(input("Por favor ingrese cantidad de segundos:"))

print(f"La cantidad de segundos ingresados es: {segundos} y la corresponde a: {segundos_a_horas(segundos)} en horas")

#Ejercicio6
#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y
# imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función


def tabla_multiplicar(numero):  
    for i in range(1,11):
   
         print(f"{numero} x {i} ={numero * i}")

numero= int(input("Por favor ingrese un numero entero:"))

tabla_multiplicar(numero)

#Ejercicio7
#Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.


def operaciones_basicas(a,b):
    while a<=b:
        print("el primer numero debe ser mayor que el segundo")
        a=int(input("Por favor ingrese el numero a:"))
        b= int(input("Por favor ingrese el segundo numero para b:"))

    suma = a+b
    multiplicacion=a*b
    division=a//b
    resta= a-b 

    return suma, multiplicacion, division, resta

a=int(input("Ingrese el numero a:"))
b=int(input("Ingrese un numero para b:"))

suma, multiplicacion, division, resta=operaciones_basicas(a,b)
# Mostrar los resultados de forma clara
print(f"La suma es:{suma}")
print(f"La multiplicacion es:{multiplicacion}")
print(f"La division es:{division}")
print(f"La resta es:{resta}")

#Ejercicio8
#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    return peso/(altura**2)

peso=float(input("Por favor ingrese su peso en kg:"))
altura=float(input("Por favor ingrese su altura en metros:(ejemplo:1.58)"))

imc= calcular_imc(peso,altura)
print(f"Su indice de masa corporal es:(imc) es: {imc:.2f}")

#ejercicio9
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius
#  y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función
def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8)+23

celsius=int(input("Ingrese la temperatura en celsius:"))

faherenheit= celsius_a_fahrenheit(celsius)
print(f"La temperatura que ingreso es equivalente en fahrenheit a: {faherenheit}")

#ejercicio10
#.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos.
 #Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    return (a+b+c)/3

a=int(input("Por favor ingrese la nota numero 1:"))
b=int(input("Por favor ingrese la nota numero 2:"))
c=int(input("Por favor ingrese la nota numero 3:"))

promedio=calcular_promedio(a,b,c)

print(f"El promedio de las notas ingresadas es: {promedio}")