import Nodoterreno

class Simple():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        

    def Creart(self,nombre,dimx,dimy,inix,iniy,finx,finy):
        nuevo = Nodoterreno.terreno(nombre,dimx,dimy,inix,iniy,finx,finy)
        self.size += 1 
        if self.primero is None:
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    
    def ImprimirT(self):
        aux = self.primero
        while aux is not None:
            print(aux.nombre)

    def getTerreno(self,nombre):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente
        return None
        
