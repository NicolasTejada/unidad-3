import numpy as np

from claseContratos import contrato

from claseJugador import Jugador


class arregloNumPy:
    __cantidad=0
    __dimension=0
    __incremento=10
    
    
    def __init__(self, dimension, incremento=10):
        self.__contratos=np.empty(dimension, dtype=contrato)
        self.__dimension=dimension
        self.__cantidad=0
        
        
    def agregarContrato(self, unContrato):
        if (self.__cantidad==self.__dimension):
            self.__dimension+=self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad]=unContrato
        self.__cantidad+=1
            
        
        
        
    def mostrarDatos(self):
        for i in range(len(self.__contratos)):
            print(self.__contratos[i])
            
            
    def testContrato(self, equipo, jugador):
       fechainicio=input("Ingrese la fecha de inicio del contrato")
       fechadefinalizacion=input("Ingrese la fecha de finalizacion del contrato")
       sueldo=input("Ingrese el pago mensual del contrato")
       
       
       unContrato=contrato(fechainicio, fechadefinalizacion, sueldo, equipo, jugador)
       self.agregarContrato(unContrato)
       
       
       
       


        
        