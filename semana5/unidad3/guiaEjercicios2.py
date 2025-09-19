# 1. Cargar y mostrar array
n = 5
array = [0] * n
for i in range(n):
    array[i] = int(input(f"Ingresa un numero ({i+1}/{n}):"))
print("Contenido del array: ")
for i in range(n):
    print(array[i], end=" ")
print("\n")

# 2. Sumar todos los elementos
n = 10
array = [0] * n
suma = 0 
for i in range(n): 
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
    suma +=array[i]
print("La suma de los elementos es:", suma, "\n")

# 3. Promedio de valores
n = 6
array = [0.0] * n
suma = 0 
for i in range(n):
    array[i] = float(input(f"ingresa un numero real ({i+1}/{n}): "))
    suma += array[i]
print("El promedio es:", suma / n, "\n")

# 4. Contar mayores a un valor

n= 8
array = [0] * n
contador = 0 
for i in range(n): 
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
    if array[i] >  100:
        contador += 1
print("Cantidad de numeros mayores a 100:", contador, "\n")

# 5. Buscar un valor 
n = 10
array = [0] * n 
for i in range(n):
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
valor = int(input("ingrese el valor a buscar: "))
pos = -1
for i in range(n):
    if array[i] == valor: 
        pos = i 
        break
if pos != -1:
    print(f"Valor encontrado en la posicion {pos}")
else:
    print("El valor no se encuentra en el array")
print()

# 6. Mayor y su posicion
n = 7
array = [0] * n
for i in range(n):
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
mayor = array[0]
pos = 0 
for i in range(1, n):
    if array[i] > mayor:
        mayor = array[i]
        pos = i
print(f"el mayor es {mayor} y esta en la posicion {pos}\n")

# 7. invertir orden

n = 6
array = [0] * n
for i in range(n): 
    array[i] = int(input(f"Ingrese un numero ({i+1}/{n}): "))
print("array invertido: ")
for i in range(n-1, -1, -1):
    print(array[i], end=" ")
print("\n")

# 8. Comparar dos arrays

n = 5 
array1 = [0] * n
array2 = [0] * n
print("Cargar primer array: ")
for i in range(n):
    array[i] = int(input(f"Ingrese un numero ({i+1}/{n}): "))
print("Cargar segundo array: ")
for i in range(n):
    array2[i] = int(input(f"Ingresa un numero ({i+1}/{n}): "))

iguales = True
for i in range(n):
    if array1[i] != array2[i]: 
        iguales = False
        break
if iguales: 
    print("Los arrays son iguales\n")
else:
    print("Los arrays No son iguales\n")

# 9. Intercambiar elementos pares por ceros
n = 10
array = [0] * n
for i in range(n):
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
    if array[i] % 2 == 0:
        array[i] = 0
print("Array resultante con pares reemplazados por cero: ")
for i in range(n): 
    print(array[i], end=" ")
print("\n")

# 10. Funcion para buscar la primera aparicion de un valor
def buscar_aparicion(array, valor): 
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1


# prueba de la funcion
n = 7
array = [0] * n
for i in range(n):
    array[i] = int(input(f"ingresa un numero ({i+1}/{n}): "))
valor = int(input("Ingresa un numero a buscar: "))
pos = buscar_aparicion(array, valor)
if pos!= -1:
    print(f"el numero {valor} aparece por primera vez en la posicion {pos}")
else: 
    print("El numero no se encuentra en el array")


