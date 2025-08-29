precio_montaña = 1500
precio_casa = 1200
precio_carrusel = 800

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
cantidad= int(input("Cuantas atracciones quiere usar "))

montaña_elegida = False
casa_elegida = False
carrusel_elegida = False

costo_total = 0 

for i in range(cantidad): 
    print("atracciones disponibles: Montaña Rusa, Casa del Terror, Carrusel")
    eleccion = input("Ingrese el nombre de la atraccion que desea usar:")

    if eleccion == "Montaña Rusa":
        if edad >= 12:
            print("Puede subir a la Montaña Rusa.")
            montaña_elegida = True
            costo_total+= precio_montaña
        else:
            print("no puede subir a la montaña debido a que no cumple el requisito de edad")
    elif eleccion == "Casa del Terror": 
        if edad >= 6:
            print("puede subir a la casa del terror.")
            casa_elegida = True
            costo_total += precio_casa
        else:
            print("no puede subir a la casa del terror debido a que no cumple el requisito de edad")
    elif eleccion == "carrusel":
        print("puede subir al carrusel")
        carrusel_elegida = True
        costo_total += precio_carrusel
    else:
        print("no existe esa atraccion")

    print(" RESUMEN VISITA ")
    print(f"Nombre: {nombre}")
    print("Atracciones que pudo usar: ")
    if montaña_elegida:
        print("- Montaña Rusa")
    if casa_elegida:
        print("- Casa del Terror")
    if carrusel_elegida:
        print("- Carrusel")
    print(f"Costo total a pagar: ${costo_total}")
