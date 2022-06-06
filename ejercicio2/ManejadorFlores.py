import numpy as np 

import csv 

from claseFlores import Flores


class arregloNumPy:
    __cantidad= 0
    __dimension=0
    __incremento=5
    
    
    def __init__(self, dimension, incremento=5):
        self.__flores=np.empty(dimension, dtype= Flores)
        self.__cantidad=0
        self.__dimension=dimension
        
        
    def AgregarFlor(self, unaFlor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad]=unaFlor
        self.__cantidad+= 1
        
    def Mostrardatos(self):
        
        for i in range(len(self.__flores)):
                            
            print(self.__flores[i])
            
    def getFlor(self, clave):
        
        band=False
        i=0
        while not band:
            if self.__flores[i].getnombre == clave:
                i+=1
                band=True
        return self.__flores[i]
                
    def testFlores(self):
        
        archivo= open('flores.csv')
        reader= csv.reader(archivo, delimiter=',')
        
        
        for fila in reader:
            
            numero = int( fila[0]) 
            nombre= fila[1]  
            color= fila[2]
            descripcion= str(fila[3])
            
            
            unaFlor= Flores(numero, nombre, color, descripcion)
            
            self.AgregarFlor(unaFlor)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            