#Librerias
import xml.etree.ElementTree as et  
import time
from Nodo import *
from Nodoterreno import *
from Simple import *
from Doble import *
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
lista = doble()
url = ""
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
                
                procesar()
            
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
    print(V+"Terrenos disponibles: "+Mo)
    
    b = None
    if b != listaterr.ImprimirT():
        RESET
    else:
        print()    
    a = input(RESET+"Ingrese el terreno a trabajar ")
        
    print("No funciono :c")
    menu()
def test():
    a = input("Ingrese la ruta del archivo ")
    global url
    url = a 
    
    tree = et.parse(a)
    root = tree.getroot()
    
    print("Iniciando carga de archivo...")
    print('\nArchivo Cargado')
    for elemento in root: 
        nombre = elemento.get('nombre')
        #print(Nodoterreno.nombre)
        
        
        for dim in elemento.iter('m'):
            dimx = dim.text
            
        for dim in elemento.iter('n'):
            dimy = dim.text
            
        for lptm3 in elemento.iter('posicioninicio'):
            for dim2 in lptm3.iter('x'):
                inix = dim2.text
            for dim2 in lptm3.iter('y'):
                iniy = dim2.text
                
        for lptm4 in elemento.iter('posicionfin'):
            for dim3 in lptm4.iter('x'):
                finx = dim3.text
            for dim3 in lptm4.iter('y'):
                finy = dim3.text
                
        listaterr.Creart(nombre,dimx,dimy,inix,iniy,finx,finy)
        for lptm in elemento.iter('posicion'):
            
            mapa = listaterr.getnom(nombre)
            
            mapa.lista_pos.agregar(lptm.attrib['x'],lptm.attrib['y'],lptm.text)
        
            
    menu()
    



def archivosalida():
    print("Estoy en mantenimiento, no seguir")


    menu()

def gg():
    print(V+"Terrenos disponibles: "+Mo)
    global url
    
    b = None
    if b != listaterr.ImprimirT():
        RESET
    else:
        print()    
    a = input(str(RESET+"Ingrese el terreno a trabajar "))
    graphviz='''
    digraph L{
    node[shape=cylinder fillcolor="#FFEDBB" style =filled]
    
    subgraph cluster_p{
        fontsize = 50
        label= " '''+a+''' "
        bgcolor = "lavender"
        edge[dir = "none"]


    '''
    graphi = """
    }

}
"""
    
    tree = et.parse(url)
    root = tree.getroot()
    try:
        print(R+"\nEmpezando a generar la gráfica"+RESET)
        for elemento in root: 
           nombre = elemento.get('nombre')
           
           if nombre == a:
            for subelemento in elemento: 
           
                for lptm in subelemento.iter('posicion'):
               
                    #print('x: '+lptm.attrib['x']+' y: '+ lptm.attrib['y']+' valor:'+ lptm.text)
                        posx = lptm.attrib['x']
                        posy = lptm.attrib['y']
                        gas = lptm.text
                        b = str(str(posx)+"_"+str(posy))
                        graphviz += "\nnodo"+b+"[label= "+""+gas+""+" ,fillcolor=cyan,group="+str(posx)+"]"
                for lptm2 in subelemento.iter('dimension'):
                    for dim in lptm2.iter('m'):
                        x = int(dim.text)
                    for dim in lptm2.iter('n'):
                        y = int(dim.text)
        


   

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
        f= open(''+a+'.dot','w')
        f.write(graphviz)
        f.close()
        system('dot -Tpng '+a+'.dot -o '+a+'.png')
        system('cd ./'+a+'.png')
        startfile(''+a+'.png')
        menu()
    except:
        print(R+"Ha ocurrido un error... Regresando al menú"+RESET)
        menu()



#Codigo
print(V+"\nBienvenido a la agencia Guatemalteca de Investigación Espacial")
print("Ingresando al menú")
menu()