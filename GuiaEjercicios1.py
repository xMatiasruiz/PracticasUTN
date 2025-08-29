
 # 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
# un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función 

def saludar(nombre):
    print("Hola", nombre, "Bienvenido!!")
usuario = input("Cual es tu nombre? ")
saludar(usuario)

# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
#resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
#función.


def operaciones(num1,num2):
    print("suma",  num1 + num2)
    print("resta",  num1 - num2)
    print("multiplicacion:", num1 * num2)

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

operaciones(numero1, numero2)

#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
#devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
#Fórmula: area = (b * h) / 2.

def area_triangulo(base, altura):
    print("area", (base*altura) / 2)

b = float(input("ingrese la base: "))
a = float(input("ingrese la altura: "))

area_triangulo(b, a)

#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
#ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
#ordenados.


def buscar_mayor(a,b,c):
    if a >=b and a>=c:
        if b>=c:
            return a,b,c
        else:
            return a,c,b
    elif b>= a and b >= c:
        if a >=c:
            return b,a,c
        else:
            return b,c,a
    else: 
        if a >= b:
            return c,a,b
        else:
            return c,b,a
        

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

resultado = buscar_mayor(n1,n2,n3)
print("Numeros ordenados", resultado)

#5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.

def es_par(numero): 
    return numero % 2 == 0

num = int(input("Ingrese un numero: "))
if es_par(num):
    print(num, "es_par")
else:
    print(num, "es_impar")

#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran

def convertir_minutos(minutos): 
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Ingrese la cantidad de minutos: "))
h,m = convertir_minutos(minutos)
print(f"{minutos} minutos son {h} horas y {m} minutos")





#7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y 
#determine si es mayor de edad (18 años o más) devolviendo un booleano.
#Luego, el programa debe pedir la edad al usuario y mostrar un mensaje apropiado.

def verificar_acceso(edad):
    return edad >=18

edad = int(input("Ingrese su edad: "))
if verificar_acceso(edad):
    print("sos mayor de edad")
else:
    print("sos menor de edad")
#8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
#devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
#año de nacimiento del usuario y mostrar la edad calculada.

def calcular_edad(anio_nacimiento):
    año_actual = 2025
    return año_actual - anio_nacimiento

user= int(input("En que año naciste? "))

edad= calcular_edad(user)
print("Tu edad es: ", edad)

