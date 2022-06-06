import csv

import numpy as np

from claseEquipo import Equipo


class arregloNumPy:
    __cantidad=0
    __dimension=0
    __incremento=5
    
    def __init__(self, dimension, incremento=5):
        self.__Equipos= np.empty(dimension, dtype= Equipo)
        self.__dimension=dimension
        self.__cantidad=0
        
    def agregarEquipo(self, unEquipo):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__Equipos.resize(self.__dimension)
            
        self.__Equipos[self.__cantidad]=unEquipo
        self.__cantidad+=1
    
    def mostrarDatos(self):
        for i in range(len(self.__Equipos)):
            print(self.__Equipos[i])
    
    def getEquipo(self, equipo):
        
        i=0
        band=False
        while not band and i<self.__cantidad:
            if self.__Equipos[i].getNombre==equipo:
                
                band=True
                print("exito")
            i+=1
        if not band:
            print('No se encontro el equipo ')
        return self.__Equipos[i]
                               
            
        
    def testEquipo(self):
        archivo=open("Equipos.csv")
        reader=csv.reader(archivo, delimiter=",")
        
        for fila in reader:
            nombre=fila[0]
            ciudad=fila[1]
            
            unEquipo=Equipo(nombre, ciudad)
            
            self.agregarEquipo(unEquipo)
            
            