#Librerias
import xml.etree.ElementTree as et  
import time
import Nodo 
import Nodoterreno
#Variabl-es
N = '\033[30m'
R = '\033[31m'
V = '\033[32m'
Am = '\033[33m'
Az = '\033[34m'
Mo = '\033[35m'
C = '\033[36m'
Bl = '\033[37m'
RESET = '\033[39m'
Nomme = []
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
        if (a <= 0 or a>= 7):
            print("El numero ingresado es invalido, ingrese un numero entre 1 y 6")
            menu()
        if (a == 1):
            test()
           
        if (a == 2):
           print("Ya se cargó el archivo")
         
        if (a == 3):
            archivosalida()           
        if (a == 4):
            datos()
        if (a == 5):
           print("Ya se cargó el archivo")
           menu()
        if (a == 6):
            print("Saliendo...")
    except: 
        print("Ha ingresado un caracter invalido")
        menu()

def datos():
    print("""
                                                                                                         
"""+R+"""   (                                          (               (                )                         
   )\       )   (     (  (       )            )\ )            )\ )      )   ( /(                         
 (((_)   ( /(   )(    )\))(   ( /(    (      (()/(    (      (()/(   ( /(   )\())   (    (               
 )\ """+C+"""__ """+R+"""  )(_)) (()\  ((_))\   )(_))   )\ )    (("""+C+"""_"""+R+"""))   )\      (("""+C+"""_"""+R+"""))  )(_)) ("""+C+"""_"""+R+"""))/    )\   )\              
(("""+C+"""/ __|"""+R+""" (("""+C+"""_"""+R+""")"""+C+"""_"""+R+"""   (("""+C+"""_"""+R+""")  (()("""+C+"""_"""+R+""") (("""+C+"""_"""+R+""")"""+C+"""_   _"""+R+"""("""+C+"""_"""+R+"""/(    """+C+"""_| |"""+R+"""   (("""+C+"""_"""+R+""")     """+C+"""_| |"""+R+"""  (("""+C+"""_"""+R+""")"""+C+"""_  | |_"""+R+"""    (("""+C+"""_"""+R+""") (("""+C+"""_"""+R+""")             
 """+C+"""| (__  / _` | | '_| / _` |  / _` | | ' ')) / _` |  / _ \   / _` |  / _` | |  _|  / _ \ (_-<  _   _   _  
  """+C+"""\___| \__,_| |_|   \__, |  \__,_| |_||_|  \__,_|  \___/   \__,_|  \__,_|  \__|  \___/ /__/ (_) (_) (_) 
  """+C+"""                   |___/    
                     
    """)
    time.sleep(3)
    print(C+"╔ ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙ "+V+"Datos del estudiante"+C+" ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙ ╗"+RESET)
    print(C+"║"+Mo+" Nombre: "+V+"Pedro Alejandro Zetino Páez"+C+"                                            ║")
    print(C+"║"+Mo+" Carnet: "+V+"202004750"+C+"                                                              ║")
    print(C+"║"+Mo+" Curso: "+V+"LABORATORIO INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 Sección D"+C+"    ║")
    print(C+"║"+Mo+" Carrera: "+V+"Ingenieria en ciencias y sistemas"+C+"                                     ║")
    print(C+"║"+Mo+" Semestre: "+V+"4to"+C+"                                                                  ║")
    print(C+"╚ ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙ ╝"+RESET)
    print("                   ")
    time.sleep(2)
    menu()

def abrir():
    a = input("Ingrese la ruta del archivo ")
    tree = et.parse(a)
    root = tree.getroot()
    for hijo in root:
        #Nodoterreno.nombre = terreno.attrib['Nombre']
        #Nodoterreno.dimx = terreno.attrib['']
        print(hijo)
    print("Toy probando")
    menu()
def procesar():
    print("Estoy en desarrollo")
    
def test():
    a = input("Ingrese la ruta del archivo ")
    print(a)
    tree = et.parse(a)
    root = tree.getroot()
    

    print('\nTodos los Atributos')
    for elemento in root: 
        Nodoterreno.nombre = elemento.get('nombre')
        for subelemento in elemento: 
            
            for lptm in subelemento.iter('posicion'):
                print()
                #print('x: '+lptm.attrib['x']+' y: '+ lptm.attrib['y']+' valor:'+ lptm.text)
            
            for lptm2 in subelemento.iter('dimension'):
                for dim in lptm2.iter('m'):
                    print(dim.text)
                for dim in lptm2.iter('n'):
                    print(dim.text)
            
            for lptm2 in subelemento.iter('posicioninicio'):
                for dim in lptm2.iter('x'):
                    print(dim.text)
                for dim in lptm2.iter('y'):
                    print(dim.text)

            for lptm2 in subelemento.iter('posicionfin'):
                for dim in lptm2.iter('x'):
                    print(dim.text)
                for dim in lptm2.iter('y'):
                    print(dim.text)
"""    for elemento in root:
        print(elemento) #tag
        for subelemento in elemento:
            print('> ' + subelemento.text) #valores -> text"""


def archivosalida():
    print("Omla")
    a = input("Ingrese la ruta donde se escribirá el archivo")
    b = a+"\salida.txt"
    f = open(b,"w")
    f.write("Esto es una prueba")
    f.close

    menu()
    
#Codigo
menu()