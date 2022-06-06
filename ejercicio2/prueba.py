import numpy as np

from claseRamo import Ramo

class arregloNumPy():
    __cantidad=0
    __dimension=0
    __incremento=1
    
    def __init__(self, cantidad, dimension, incremento=1):
        self.__Ramos=np.empty(dimension, dtype=Ramo)
        self.__cantidad=0
        self.__dimension=dimension
        
    def agregarRamo(self, unRamo):
        
        if self.__cantidad==self.__dimension:
            self.__dimension+= self.__incremento
            self.__Ramos.resize(self.__dimension)
        self.__Ramos[self.__cantidad]=unRamo
        self.__cantidad+=1
        
    def Mostrardatos(self):
        
        for i in range(len(self.__Ramos)):
                            
            print(self.__Ramos[i])
            
    
    
    
    
    #prueba
    
    arregloRamo= arregloNumPy(0, 1)
    
    unRamo=Ramo('chico')
    arregloRamo.agregarRamo(unRamo)
    otroRamo=Ramo('grande')
    arregloRamo.agregarRamo(otroRamo)
    
    arregloRamo.Mostrardatos()
    
    
    
    