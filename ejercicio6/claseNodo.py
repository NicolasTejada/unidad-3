class Nodo:
    __Aparato=None
    __siguiente=None

    def __init__(self, aparato):
        self.__Aparato=aparato
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__Aparato