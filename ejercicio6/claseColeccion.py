from claseAparatosElectronicos import AparatosElectronicos

from claseNodo import Nodo

class lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration

        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato


    def agregarDato(self):
        nodo=Nodo(AparatosElectronicos)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__tope+=1

        