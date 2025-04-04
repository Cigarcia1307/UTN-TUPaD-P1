#Ejercicio1
# Pedimos al usuario que ingrese su edad
edad = int(input("Por favor ingrese su edad: "))

# Si el número es mayor a 18 imprimir es mayor de edad
if (edad >=18):
    print("Es mayor de edad")
# En cualquier otro caso, no hacer nada
else:
    pass



#Ejercicio2
# Pedimos al usuario que ingrese una nota
nota = int(input("Por favor ingrese la nota: "))

# Si el número es mayor a 6 imprimir aprobado
if (nota >=6):
    print("Aprobado")
# Si nota es menor a 6 mostrar desaprobado
else:
    print("Desaprobado")


#Ejercicio3
# Pedimos al usuario que ingrese un numero
numero = int(input("Por favor ingrese un numero: "))

# Si el número es par imprimir Ingreso un numero par
if numero % 2 == 0:
    print("Ingreso un numero par")
# Si no es par, solicitar que ingrese nuevamente
else:
    print("Por favor ingrese un numero par")

#Ejercicio4
# Pedimos al usuario que ingrese su edad
edad = int(input("Por favor ingrese su edad: "))

# Si el número es menor a 12 mostrar Categoria niño/a
if edad < 12:
    print("Categoria Niño/a")
# si ingresa >=12 y < que 18
elif 12 <= edad < 18:
     print("Categoria Adolescente")
# si ingresa >=18 y < que 30
elif 18 <= edad < 30:
    print("Categoria Adulto/a Joven")
else: # si ingresa >=30 
    print("Categoria Adulto/a")




#Ejercicio 5
# Pedimos al usuario que ingrese una contraseña
contraseña = (input("Por favor ingrese contraseña:"))
# Verificamos si la longitud está entre 8 y 14 caracteres
if 8 <= len(contraseña)<= 14:
    print ("Ha ingresado una contraseña correcta.")
else:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")


# Generar una lista de 50 numeros aleatorios entre 1 y 100
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Calcular la media, mediana y moda
moda= mode (numeros_aleatorios)
media= mean (numeros_aleatorios)
mediana= median (numeros_aleatorios)
#ver los resultados
print(f"numeros_aleatorios:{numeros_aleatorios}")
print(f"moda:{moda}")
print(f"media:{media}")
print(f"mediana:{mediana}")

if media< mediana and mediana < moda:
    print("Sesgo negativo")
elif media< mediana and mediana >moda:
    print("Sesgo positivo")
elif media== mediana== moda:
    print("Sin sesgo")
else:
    pass


#Ejercicio 7
# Pedimos al usuario que ingrese una palabra
palabra = input("Por favor ingrese una palabra:")

vocales= "aeiouAEIOU"
termina_en_vocal= palabra[-1] in vocales
#Mostrar en pantalla
if termina_en_vocal:
    print(f"{palabra}!")
else:
    print(palabra)



#Ejercicio 8
# Pedimos al usuario que ingrese su nombre
nombre= input("Por favor ingrese su nombre:")
#Le damos opciones al usuario
print("Seleccione una opcion:")
print("1- Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2- Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3- Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
#Le pedimos al usuario ingrese la opcion
opcion= input("Ingrese el numero de la opcion:")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.title())
elif opcion =="3":
    print(nombre.lower())
else:
    pass

#Ejercicio9
 #Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#Menor que 3: "Muy leve" (imperceptible). 
# Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). <
# Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
# Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud= int(input("Ingrese la magnitud del terremoto:"))

if magnitud <3:
    print ("Muy leve(imperceptible)")
elif magnitud >=3 and magnitud <4:
    print("Leve(ligeramente perceptible)")
elif magnitud >=4 and magnitud <5:
    print("Moderado(sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud <6:
    print("Fuerte(puede causar daños en estructuras débiles)")
elif magnitud>= 6 and magnitud<7:
    print("Muy fuerte(Puede causar daños significativos)")
else:
    print("Extremo")

#Ejercicio10
#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 

#Periodo del año 
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos) 
#Estación en el hemisferio norte --Invierno 
#Estación en el hemisferio sur -- Verano

#Desde el 21 de marzo hasta el 20 de junio (incluidos) 
#Estación en el hemisferio norte --Primavera 
#Estación en el hemisferio sur -- Otoño

#Desde el 21 de junio hasta el 20 de septiembre (incluidos) 
#Estación en el hemisferio norte --Verano 
#Estación en el hemisferio sur --Invierno

#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
#Estación en el hemisferio norte --Otoño 
#Estación en el hemisferio sur --Primavera

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, in

#Pedimos al usuario que informe en que hemisferio se encuentra
print("Por favor ingrese en que Hemisferio se encuentra:")
print("1-Norte")
print("2-Sur")

#Le pedimos ingrese la opcion en numero
opcion=int(input("Ingrese el numero de la opcion:"))

#Ingrese en que fecha se encuentra segun opciones
print("Le pedimos nos informe la fecha actual:")
print("3- Si la fecha esta entre el 21 de diciembre al 20 de marzo inclusive")
print("4- Si la fecha esta entre el 21 de marzo al 21 de junio inclusive")
print("5- Si la fecha esta entre el 21 de junio al 20 de septiembre inclusive")
print("6- Si la fecha esta entre el 21 de septiembre al 20 de de diciembre inclusive")
fecha= int(input("Ingrese el numero de la fecha:"))

#Determinamos que estacion es


if opcion == 1: #Norte

    if fecha == 3:
        print(" Se encuentra en: Invierno")
    elif fecha == 4:
        print("Se encuentra en: Primavera")
    elif fecha == 5:
        print (" Se encuentra en: Verano")
    elif fecha == 6:
        print("Se ecuentra en: Otoño")
elif opcion == 2: #Sur

    if fecha == 3:
        print("Se encuentra en: Verano")
    elif fecha == 4:
        print("Se encuentra en: Otoño")
    elif fecha == 5:
        print(" Se encuentra en: Invierno")
    elif fecha == 6:
        print("Se encuentra en: Primavera")
else:
    print("Ingreso numeros incorrectos") 



