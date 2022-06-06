
class Flores():
    
    __Numero=00
    __Nombre=""
    __Color=""
    __Descripcion=""
    
    
    def __init__(self,numero, nombre,  color, desc):
        self.__Numero=numero
        self.__Nombre=nombre
        self.__Color=color
        self.__Descripcion=desc
        
        
    def __str__(self):
        return ('Nombre{} Numero: {}, Color: {} Descripcion: {} \n'.format(self.__Nombre , self.__Numero, self.__Color, self.__Descripcion))
        
    def getnombre(self):
        return self.__Nombre