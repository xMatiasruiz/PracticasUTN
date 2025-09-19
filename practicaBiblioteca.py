Max_libros = 20
titulos = [""] * Max_libros
ejemplares = [0] * Max_libros
contador = 0

def cargar_titulos(titulos,ejemplares, contador):
    if contador >= Max_libros:
        print("No se pueden cargar mas libros, catalogo lleno")
        return contador
    
    n=int(input(f"Cuantos libros quiere ingresar?(max.{Max_libros - contador}): "))
    for i in range(n):
        if contador < Max_libros: 
            titulo = input("Titulo del libro: ")
            copias = int(input("Cuantos ejemplares?: "))
            titulos[contador] = titulo
            ejemplares[contador] = copias
            contador += 1
        else:
            print("Limite alcanzado.")
            break
    return contador

def mostrar_catalogo(titulos, ejemplares,contador):
    if contador == 0:
        print("No hay libros cargados.")
    else:
        print("CATALOGO COMPLETO")
        for i in range(contador):
            print(f"{titulos[i]} tiene {ejemplares[i]} copias ")

def consultar_disponibilidad(titulos,ejemplares, contador):
    buscar= input("Titulo que desee buscar? ")
    for i in range(contador): 
        if titulos[i].lower() == buscar.lower():
            print(f"{titulos[i]} tiene {ejemplares[i]} copias disponibles")
            return
    print("libro no encontrado")

def listar_agotados(titulos, ejemplares, contador): 
    print("Libros agotados")
    vacio = True
    for i in range(contador):
        if ejemplares[i] == 0:
            print(f"{titulos[i]}")
            vacio= False
        if vacio:
            print("no hay libros agotados")

def agregar_nuevo(titulos,ejemplares, contador):
    if contador >= Max_libros: 
        print("No se pueden agregar mas titulos, catalogo lleno")
        return contador
    
    titulo = input("Ingrese titulo nuevo: ")
    copias = int(input("Ingrese cantidad de ejemplares: "))
    titulos[contador] = titulo
    ejemplares[contador] = copias
    contador += 1 
    print("Libro agregado correctamente.")
    return contador

def actualizar_ejemplares(titulos, ejemplares, contador):
    buscar = input("Titulo a actualizar: ")
    for i in range(contador):
        if titulos[i].lower() == buscar.lower():
            print(f"ejemplares actuales: {ejemplares[i]}")
            nuevo = int(input("ingrese nueva cantidad de ejemplares: "))
            ejemplares[i] = nuevo
            print("Cantidad actualizada.")
            return
    print("Libro no encontrado.")


def menu():
    titulos = [""] * Max_libros
    ejemplares = [0] * Max_libros
    contador = 0

    while True:
        print("--MENU--")
        print("1. Cargar titulos y ejemplares")
        print("2. Mostrar catalogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar titulos agotados")
        print("5. Agregar un nuevo titulo")
        print("6. Actualizar ejemplares")
        print("7.Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1": 
            contador = cargar_titulos(titulos, ejemplares, contador)
        elif opcion == "2":
            mostrar_catalogo(titulos, ejemplares, contador)
        elif opcion == "3":
            consultar_disponibilidad(titulos,ejemplares,contador)
        elif opcion == "4":
            listar_agotados(titulos,ejemplares,contador)
        elif opcion == "5":
            contador = agregar_nuevo(titulos,ejemplares,contador)
        elif opcion == "6":
            actualizar_ejemplares(titulos,ejemplares,contador)
        elif opcion == "7":
            print("Saliendo del sistema. . .")
            break
        else:
            print("Opcion incorrecta, intente de nuevo.")

menu()