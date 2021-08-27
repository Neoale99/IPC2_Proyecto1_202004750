#Librerias
import xml.etree.ElementTree as et  
import time
import Nodo 
import Nodoterreno
import Simple
import Doble
from os import system,startfile
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
listaterr = Simple()
listdob = Doble()
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
           gg()
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


def procesar():
    print("Ingrese el nombre del terreno a trabajar: ")
    
def test():
    a = input("Ingrese la ruta del archivo ")
    print(a)
    tree = et.parse(a)
    root = tree.getroot()
    

    print('\nTodos los Atributos')
    for elemento in root: 
        nombre = elemento.get('nombre')
        #print(Nodoterreno.nombre)
        for subelemento in elemento: 
            

            for lptm2 in subelemento.iter('dimension'):
                for dim in lptm2.iter('m'):
                    dimx = dim.text
                
                for dim in lptm2.iter('n'):
                    dimy = dim.text
            
            for lptm2 in subelemento.iter('posicioninicio'):
                for dim2 in lptm2.iter('x'):
                    inix = dim2.text
                for dim2 in dim2.iter('y'):
                    iniy = dim2.text

            for lptm2 in subelemento.iter('posicionfin'):
                for dim3 in lptm2.iter('x'):
                    finx = dim3.text
                for dim3 in lptm2.iter('y'):
                    finy = dim3.text

            listaterr.Creart(nombre,dimx,dimy,inix,iniy,finx,finy)
            for lptm in subelemento.iter('posicion'):
                print()
                print('x: '+lptm.attrib['x']+' y: '+ lptm.attrib['y']+' valor:'+ lptm.text)
                mapa = elemento.get('nombre')
                mapa.lista_pos.agregar(lptm.attrib['x'],lptm.attrib['y'],lptm.text)
    
    menu()



def archivosalida():
    print("Omla")
    a = input("Ingrese la ruta donde se escribirá el archivo")
    b = a+"\salida.txt"
    f = open(b,"w")
    f.write("Esto es una prueba")
    f.close

    menu()

def gg():
    graphviz='''
    digraph L{
    node[shape=box fillcolor="#FFEDBB" style =filled]
    
    subgraph cluster_p{
        label= "TERRENO "
        bgcolor = "#398D9C"
        edge[dir = "none"]


    '''
    graphi = """
    }

}
"""
    a = input("Ingrese la ruta del archivo ")   
    print(a)
    tree = et.parse(a)
    root = tree.getroot()
    
    print('\nTodos los Atributos han sido cargados')
    for elemento in root: 
       
       #print(Nodoterreno.nombre)
       for subelemento in elemento: 
           
           for lptm in subelemento.iter('posicion'):
               continue
               #print('x: '+lptm.attrib['x']+' y: '+ lptm.attrib['y']+' valor:'+ lptm.text)
           
           for lptm2 in subelemento.iter('dimension'):
               for dim in lptm2.iter('m'):
                   x = int(dim.text)
               for dim in lptm2.iter('n'):
                   y = int(dim.text)



    for i in range(x):
        i = i+1
        for o in range(y):
            o = o+1
            b = str(str(i)+"_"+str(o))
            graphviz += "\nnodo"+b+"[label= "+"gas"+" ,fillcolor=green,group="+str(i)+"]"

    for i in range(x-1):
        i = i+1
        for o in range(y):
            o = o+1
            b = str(str(i)+"_"+str(o))
            c = str(str(i+1)+"_"+str(o))
            graphviz += "\nnodo"+b+"->nodo"+c+""

    for i in range(x):
            i = i+1
            for o in range(y-1):
                o = o+1
                b = str(str(i)+"_"+str(o))
                c = str(str(i)+"_"+str(o+1))
        
                graphviz +=  "\n{rank=same;nodo"+b+"->nodo"+c+"}"

    graphviz += "\n"+graphi
    menu()

#Codigo
menu()