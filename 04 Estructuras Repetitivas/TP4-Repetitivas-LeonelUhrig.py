# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador = 0
# mas sencillo pero no es estructura repetitiva> print("La cantidad de dígitos es:", len(str(numero)))
while numero > 0:
    numero //= 10
    contador += 1
print("La cantidad de dígitos es:", contador)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = 0
if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        suma += i
else:
    for i in range(numero2 + 1, numero1):
        suma += i
print(f"La suma de los números enteros comprendidos entre {numero1} y {numero2} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = int(input("Ingrese un número entero (0 para salir): "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para salir): "))
print(f"La suma total acumulada es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero = random.randint(0, 9)
intentos=1
numero_usuario = int(input("Adivina el número entre 0 y 9: "))
while numero_usuario != numero:
    numero_usuario = int(input("intenta nuevamente: "))
    intentos += 1    
print(f"¡Felicidades! Adivinaste el número {numero} en {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i
print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

media = 0
suma = 0
for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
media = suma / 100
print(f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print(f"El número invertido es: {numero_invertido}")