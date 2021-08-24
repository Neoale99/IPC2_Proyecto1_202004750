from Nodo import Nodo


import Nodo

class Simple:
    def __init__(self):
        self.primero = None

    def insertar(self,nombre,dimx,dimy,inix,iniy,finx,finy):
        nuevo = None
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def mostrarnodo(self):
        tmp = self.primero
        while tmp is not None:
            print()
        
