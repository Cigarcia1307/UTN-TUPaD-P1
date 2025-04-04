print("Hola Mundo")
#ejercicio 2
nombre=input("Ingrese su nombre por favor:")
print(f"Hola {nombre}!")
#ejercicio3
nombre=input("Por favor ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=int(input("Ingrese su edad:"))
residencia=input("Ingrese lugar de residencia:")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#ejercicio4
radio=int(input("Ingrese el radio:"))
pi=3.14
perimetro=2*pi*(radio)
area=pi*(radio**2)
print (f"El area es: {area} y el perimetro es: {perimetro}")

#ejercicio5
hora=3600
minutos=60
segundos=float(input("Ingrese cantidad de segundos:"))
print (f"Los segundos ingresados corresponden a {(segundos)/hora} horas")

#ejercicio6
numero=int(input("Ingrese un numero:"))
for i in range (1,11):
    multiplicar = i * numero
    print(multiplicar)
#ejercicio7
numero_a=int(input("Por favor ingrese un numero entero distinto a cero:"))
numero_b=int(input("Por favor ingrese otro numero entero distinto a cero:"))
suma=(numero_a+numero_b)
resta=(numero_a-numero_b)
multiplicar=(numero_a*numero_b)
dividir=(numero_a/numero_b)
print ("La suma de ambos es:", suma)
print ("La resta de ambos es:", resta)
print ("La multiplicacion de ambos es:", multiplicar)
print ("La division de ambos es:", dividir)
#ejercicio8
print("Para calcular su IMC, le pediremos unos datos")
peso=float(input("Por favor ingrese su peso:"))
altura=float(input("Por favor ingrese su altura:"))
imc=peso/(altura**2)
print ("La IMC es:", imc)
#ejercicio9
print("Para calcular la temperatura en Fahrenheit")
celsius=float(input("Por favor ingrese la temperatura en grados Celsius:"))
fahrenheit=9/5*celsius+32
print ("La temperatura en Fahrenheit es:", fahrenheit)
#ejercicio10
print ("Para calcular promedio le vamos a solicitar lo siguiente:")
a= float(input("Por favor ingrese un numero:"))
b= float(input("Por favor ingrese otro numero:"))
c= float(input("Por favor ingrese el ultimo numero:"))
promedio=(a+b+c)/3
print ("El promedio de los 3 numeros ingresados es:", promedio)
