from claseCarrera import Carrera


listaCarreras=[]

class Facultad():
    __Codigo=""
    __Nombre=""
    __Direccion=""
    __Localidad=""
    __Telefonno=""
    __Carreras=""
    
    def __init__(self, codigo, nomb, dirre, loca, telefono):
        self.__Codigo=codigo
        self.__Nombre=nomb
        self.__Direccion=dirre
        self.__Localidad=loca
        self.__Telefonno=telefono
        self.__Carrera= listaCarreras
    
    def agregarCarrera(self, cod, nom, fecha, duracion, tipo  ):
        
        listaCarreras.apend(Carrera(cod, nom, fecha, duracion, tipo))