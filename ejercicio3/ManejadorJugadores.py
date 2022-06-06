import csv 

from claseJugador import Jugador





class manejadorJugadores:
    __lista=[]
    
    
    def __init__(self):
        self.__lista=[]
        
    def agregarJugador(self, unJugador):
        
        self.__lista.append(unJugador)
        
    def mostrarDatos(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
    def getJugador(self, DNI):
        i=0
        band=False
        while not band and i<len(self.__lista):
            print (DNI)
            print(self.__lista[i].getDNI())
            if (self.__lista[i].getDNI()==DNI):
                
                band=True
                print('exito')
            
            i+=1
            
        if band==False:
            print('El jugador no fue encontrado')
        return self.__lista[i-1]
        
    def testJugador(self):
        '''nombre=input("Ingrese el nombre del jugador ")
        DNI=int(input('Ingrese el DNI del jugador '))
        Ciudad=input("Ingrese la ciudad natal")
        Pais=input('Ingrese el pais de Origen')
        Nacimiento=input("Ingrese la fecha de nacimiento")
        
        
        unJugador=Jugador(nombre, DNI, Ciudad, Pais, Nacimiento)
        self.agregarJugador(unJugador)'''
        
        archivo=open('jugadores.csv')
        reader=csv.reader(archivo, delimiter=";")

        for fila in reader:
            nombre=fila[0]
            documento=int(fila[1])
            ciudad=fila[2]
            pais=fila[3]
            nacimiento=fila[4]
            
            unJugador=Jugador(nombre, documento, ciudad, pais, nacimiento)
            self.agregarJugador(unJugador)
            
            
            
            

    