import csv

import numpy as np

from claseCalefactor import Calefactor
from claseCalefactorElectrico import CalefactorElectrico
from claseCalefactorGas import CalefactorGas



class arregloNumPy:
    __cantidad=0
    __dimension=0
    __incremento=10
    
    def __init__(self, dimension, incremento=10):
        self.__Calefactores= np.empty(dimension, dtype=Calefactor)
        self.__cantidad=0
        self.__dimension=dimension
        
        
    def agregarCalefon(self, unCalefactor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__Calefactores.resize(self.__dimension)
            
        self.__Calefactores[self.__cantidad]=unCalefactor 
        self.__cantidad+=1
        
    def mostrarDatos(self):
        for i in range(len(self.__Calefactores)):
                       print(self.__Calefactores[i])
                       
                       
                       
    def testCalefactores(self):
        archivo=open('calefactor-electrico.csv')
        reader=csv.reader(archivo, delimiter=",")
        
        
        for fila in reader:
            modelo=fila[0]
            marca=fila[1]
            potencia=fila[2]
            
            
            unCalefactor=CalefactorElectrico(marca, modelo, potencia)
            self.agregarCalefon(unCalefactor)

        archivo.close()            
        
        
        archivo=open('calefactor-a-gas.csv')
        reader= csv.reader(archivo, delimiter=",")    
            
        for fila in reader:
            modelo=fila[0]
            marca=fila[1]
            matricula=fila[2]
            calorias=fila[3]
            
            
            unCalefactor=CalefactorGas(marca, modelo, matricula, calorias)
            self.agregarCalefon(unCalefactor)
        archivo.close()            
        
        