#Librerias

#Variables
N = '\033[30m'
R = '\033[31m'
V = '\033[32m'
Am = '\033[33m'
Az = '\033[34m'
Mo = '\033[35m'
C = '\033[36m'
Bl = '\033[37m'
RESET = '\033[39m'
#Metodos
def menu():
    try:
        print(Az+"╔ ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ "+Mo+"Menú"+Az+" ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ ╗"+RESET)
        print(Az+"║ "+Mo+"1. Cargar archivo "+Az+"                          ║")
        print(Az+"║ "+Mo+"2. Procesar archivo "+Az+"                        ║")
        print(Az+"║ "+Mo+"3. Escribir archivo de salida "+Az+"              ║")
        print(Az+"║ "+Mo+"4. Mostrar datos del estudiante "+Az+"            ║")
        print(Az+"║ "+Mo+"5. Generar gráfica "+Az+"                         ║")
        print(Az+"║ "+Mo+"6. Salir "+Az+"                                   ║")
        print(Az+"╚ ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ ╝"+RESET)
        print("Ingrese un numero")
        a = int(input())
        if (a <= 0 or a>= 5):
            print("El numero ingresado es invalido, ingrese un numero entre 1 y 4")
            menu()
        if (a == 1):
            print("Ya se cargó el archivo")
            menu()
        if (a == 2):
            print("Ya se cargó el archivo")
        if (a == 3):
           print("Ya se cargó el archivo")
           
        if (a == 4):
            print("Saliendo...")
        if (a == 5):
           print("Ya se cargó el archivo")
           
        if (a == 6):
            print("Saliendo...")
    except: 
        print("Ha ingresado un caracter invalido")
        menu()

#Codigo
menu()