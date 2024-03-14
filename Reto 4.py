def agregar(database):
    while True:
        try:
            newID = int(input("\nDame el ID del libro: "))
            if any(libro["ID"] == newID for libro in database):
                print("Error: El ID ya existe. Por favor, elige un ID diferente.")
                continue
            break
        except ValueError:
            print("Ingrese un número valido")
    newNombre = input("Dame el nombre del libro: ")
    newautor = input("¿Quien es el autor del libro? ")
    newgenero = input("¿Cuál es el género del libro: ")
    while True:
        try:
            newpaginas = int(input("¿Cuantás páginas tiene el libro: "))
            break
        except ValueError:
            print("Ingrese un número valido")
    while True:
        try:
            newprecio = int(input("Dame el precio del libro: "))
            break
        except ValueError:
            print("Ingrese un número valido")
    database.append({"ID": newID, "Nombre": newNombre, "Autor": newautor, "Género": newgenero, "Páginas": newpaginas, "Precio": newprecio})

    database.sort(key=lambda libro: libro["ID"])

    print("\nSe ha agregado un nuevo libro:")
    print(newNombre, "de", newautor,"\n")
    return database
def buscar(database):
    print("Desea buscar el libro por:\n1. ID\n2. Nombre\n3. Autor\n4. Género\n")
    while True:
        choose = input()
        match choose:
         case "1":
             while True:
                 try:
                     search = int(input("Ingresa el ID del Libro: "))
                     break
                 except ValueError:
                     print("Ingresa un Número valido")
             encontrado = False
             print("")
             for libro in database:
                 if search == libro["ID"]:
                     print("ID:", libro["ID"],"\b,", libro["Nombre"], "de", libro["Autor"],"\b,", libro["Género"],"\nPáginas:", libro["Páginas"]," Precio:", libro["Precio"],"\n")
                     encontrado = True
             if not encontrado:
                 print("No se encontró el libro\n")
                 break
             print("")
             break
         case "2":
             search = input("Ingrese el nombre del libro: ").lower()
             encontrado = False
             print("")
             for libro in database:
                 if search in libro["Nombre"].lower():
                     print("ID:", libro["ID"],"\b,", libro["Nombre"], "de", libro["Autor"],"\b,", libro["Género"],"\nPáginas:", libro["Páginas"]," Precio:", libro["Precio"],"\n")
                     encontrado = True
             if not encontrado:
                 print("No se encontró el libro\n")
                 break
             print("")
             break
         case "3":
             search = input("Ingrese el autor del libro: ").lower()
             encontrado = False
             print("")
             for libro in database:
                 if search in libro["Autor"].lower():
                     print("ID:", libro["ID"],"\b,", libro["Nombre"], "de", libro["Autor"],"\b,", libro["Género"],"\nPáginas:", libro["Páginas"]," Precio:", libro["Precio"],"\n")
                     encontrado = True
             if not encontrado:
                 print("No se encontró el libro\n")
                 break
             print("")
             break
         case "4":
             search = input("Ingrese el género del libro: ").lower()
             encontrado = False
             print("")
             for libro in database:
                 if search in libro["Género"].lower():
                     print("ID:", libro["ID"],"\b,", libro["Nombre"], "de", libro["Autor"],"\b,", libro["Género"],"\nPáginas:", libro["Páginas"]," Precio:", libro["Precio"],"\n")
                     encontrado = True
             if not encontrado:
                 print("No se encontró el libro\n")
                 break
             print("")
             break
         case _:
             print("Error: Ingresa un número valido")
    return
def all(database):
    i=0
    lenght = len(database)
    print("")
    while i<lenght:
        print("ID:", database[i]["ID"],"\b,", database[i]["Nombre"], "de", database[i]["Autor"],"\b,", database[i]["Género"],"\nPáginas:",database[i]["Páginas"]," Precio:",database[i]["Precio"],"\n")
        i+=1
    return
database = [{"ID": 0, "Nombre": "De la Tierra a la Luna", "Autor": "Julio Verne", "Género": "Ciencia Ficción", "Páginas": 156, "Precio": 300},
            {"ID": 1, "Nombre": "Viaje al centro de la Tierra", "Autor": "Julio Verne", "Género": "Ciencia Ficción", "Páginas": 230, "Precio": 350},
            {"ID": 2, "Nombre": "Cien años de soledad", "Autor": "Gabriel García Márquez", "Género": "Realismo Mágico", "Páginas": 420, "Precio": 510}]

while True:
    print("Bienvenido a la Librería \"El Jorjais\" ")

    print("\nMenú\nA. Agregar un nuevo libro\nB. Buscar un libro\nC. Todos los libros\nD. Salir\n")

    while True:
        choose = input().upper()
        match choose:
            case "A":
                agregar(database)
                break
            case "B":
                buscar(database)
                break
            case "C":
                all(database)
                break
            case "D":
                break
            case _:
                print("Error: Ingresa una opción valida")
    if choose == "D":
        break
