from Nodo import nodo

class doble():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar(self,x,y,comb):
        if self.vacia():
            self.primero = self.ultimo = nodo(x,y,comb)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(x,y,comb)
            self.ultimo = aux
    
    def imprimir(self):
        aux = self.primero
        while aux:
            print("x= "+str(aux.x)+" y="+str(aux.y)+" Combustible ="+str(aux.comb))
            aux = aux.siguiente

    def getin(self,x,y):
        tmp = self.primero
        while tmp is not None:
            if tmp.x == x and tmp.y == y:
                return tmp
            tmp = tmp.siguiente
        return None