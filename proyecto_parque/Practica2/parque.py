precio_montaña = 1500
precio_casa = 1200
precio_carrusel = 800



def puede_subir(edad,atraccion):
    if atraccion == "Montaña Rusa": 
        return edad >= 12
    elif atraccion == "Casa del Terror":
        return edad >= 6
    elif atraccion == "Carrusel":
        return True
    else:
        return False
    
def calcular_precio(atraccion): 
    if atraccion == "Montaña Rusa":
        return precio_montaña
    elif atraccion == "Casa del Terror":
        return precio_casa
    elif atraccion == "Carrusel":
        return precio_carrusel
    else: 
        return 0

def mostrar_atracciones():
    print("Atracciones disponibles: ")
    print("1. Montaña Rusa")
    print("2. Casa del Terror")
    print("3. Carrusel")

def registrar_visita(): 
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    cantidad = int(input("Cuantas atracciones quiere usar "))

    costo_total = 0
    atracciones_usadas = 0

    for i in range(cantidad):
        mostrar_atracciones()
        eleccion = input("Ingrese la atraccion que desea usar: ")
        if puede_subir(edad, eleccion):
            print(f"Puede subir a {eleccion}")
            costo_total += calcular_precio(eleccion)
            atracciones_usadas +=1
        else:
            print(f"No puede subir a {eleccion}")

    if atracciones_usadas >= 3:
        print("Se aplica un 10% de descuento por usar 3 o mas atracciones")
        costo_total *=0.9
    
    return nombre, edad, costo_total, atracciones_usadas

nombre, edad, total, usadas = registrar_visita() 

print(" RESUMEN DE VISITA ")
print(f"Resumen de la visita de {nombre}:")
print(f"Edad: {edad}")
print(f"Atracciones usadas: {usadas}")
print(f"Costo total: ${total}")