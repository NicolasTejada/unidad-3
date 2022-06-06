import csv

from claseFacultad import Facultad

from claseCarrera import Carrera

class manejadorFacultades():
    
    __listaFacultades=[]
    
    
    def __init__(self):
        
        self.__listaFacultades=[]
        
    def agregarFacultad(self,unaFacultad):
        self.__listaFacultades.apend(unaFacultad)
        
    def agregarCarrera(self, fac , cod, nom, fecha, duracion, tipo ):
        
        self.__listaFacultades[fac-1].__agregarCarrera(cod, nom, fecha, duracion,tipo)
        
    def testFacultad(self):
        
        archivo = open('Facultades.csv')
        reader= csv.reader(archivo, delimiter= ',')
        
        for fila in reader:
            
            if len(fila)==6:
                 codigo= fila[0]
                 nomb=fila[1]
                 dirre=fila[2]
                 loca=fila[3]
                 telefono=[5]
                 
                 unaFacultad=Facultad(codigo, nomb, dirre, loca, telefono)
                 self.agregarFacultad(unaFacultad)
           
            elif len(fila)==5:
                cod=fila[0]
                nom=fila[1]
                fecha=fila[2]
                duracion=fila[3]
                tipo=fila[4]
                self.agregarCarrera(int(cod), cod, nom, fecha, duracion, tipo)
                
            
        
        archivo.close()
        