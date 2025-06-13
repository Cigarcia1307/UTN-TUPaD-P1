#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario



def factorial_recur(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recur(numero-1)

numero=int(input("Ingrese un numero entero:"))    
print (f"El factorial de {numero} es {factorial_recur(numero)} ")  


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#specifique.

def fibonacci_recur(posicion):
    if posicion ==0:
        return 0
    elif posicion ==1:
        return 1
    else:
        return fibonacci_recur(posicion-1)+ fibonacci_recur(posicion-2)
    
posicion_ingresada=int(input("Ingrese el numero de la posiscion deseada:"))
print(f"El numero de Fibonaccio en la posicion ingresada es: {fibonacci_recur(posicion_ingresada)}")

#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recur(n,m):
    if m == 0:
        return 1
    else:
        return n*potencia_recur(n,m-1)
    
n=int(input("Ingrese un numero para la base:"))
m=int(input("Ingrese el numero para la potencia:"))
print(f" El numero {n} elevado a {m}= {potencia_recur(n,m)}")   


#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto

def decimal_binario(n):
    if n==0:
        return "0"
    elif n==1:
        return "1"
    else:
        return decimal_binario (n//2)+str(n%2)
    
numero=int(input("Ingrese un numero entero positivo:"))
print(f"El numero {numero} en binario es: {decimal_binario(numero)}")

#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es

def es_palindromo(palabra):
    if len(palabra)<=1:
        return True
    elif palabra[0] !=palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra=input("Ingrese una palabra que no contenga espacios ni tildes:")
print(f"La palaba {palabra} en palindromo es {es_palindromo(palabra)}")



#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n ==0:
        return 0
    else:
        return (n%10)+suma_digitos(n//10)
    
numero=int(input("Ingrese un numero positivo de 2 o mas digitos:"))
print(f"La suma de los digitos de:  ¨{numero} es {suma_digitos(numero)}")


#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.

def contar_bloques (n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)
    
bloque=int(input("Ingrese el numero de bloques para crear una piramide desde el numero mas bajo:"))

print(f"La cantidad de bloques que necesita para crear un piramide es: {contar_bloques(bloque)}" )


# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)



numero=int(input("Ingrese un numero entero positivo:"))
digito=int(input("Ingrese el digito que desea buscar del numero anterior ingresado(entre 0 y 9):"))

print(f"En el número {numero}, el dígito {digito} se repite {contar_digito(numero, digito)} veces.")