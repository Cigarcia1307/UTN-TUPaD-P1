
#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplo_4=[num for num in range (1,101) if num % 4==0]
   

print(multiplo_4)

# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

lista = ["computadora", "mousse", "teclado", "auriculares", "camara"]

penultimo= lista[-2]
print(penultimo)

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
notas = []
notas.append (8) 
notas.append(7.3)
notas.append(4)
print("La lista vacia se actualizo con las siguientes notas:",notas)

# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente. Imprimir la lista resultante por pantalla. 

animales = ["perro", "gato", "conejo", "pez"]
animales [1]="loro"
animales [3]= "oso"
print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#El siguiente programa lo que hace es remover el max valor de la lista dada.
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros
lista = [num for num in range(10,35,5)]
print(lista[:2])

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1]= "cronos"
autos[2]="peugeot208"
print(autos)

# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
#  Imprimir la lista resultante por pantalla
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

#Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"

#Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# Imprimir la lista resultante por pantalla
print(compras)

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
lista_anidada=[15,True, [25.5,57.9,30.6], [False]]
print(lista_anidada)
