from Doble import *
class terreno():
    def __init__(self,nombre,dimx,dimy,inix,iniy,finx,finy) :
        self.nombre = nombre
        self.dimx = dimx
        self.dimy = dimy
        self.inix = inix
        self.iniy = iniy
        self.finx = finx 
        self.finy = finy
        self.lista_pos = doble()
        self.siguiente = None
        
        