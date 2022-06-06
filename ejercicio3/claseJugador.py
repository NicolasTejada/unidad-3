class Jugador:
    __nombre=""
    __DNI=00
    __CiudadNatal=""
    __PaisOrigen=""
    __FechaNacimiento=""
    
    
    def __init__(self, nombre, documento, ciudad, pais, nacimiento):
        self.__nombre=nombre
        self.__DNI=documento
        self.__CiudadNatal=ciudad
        self.__PaisOrigen=pais
        self.__FechaNacimiento= nacimiento
        
    def __str__(self):
        return '{},  {}, {}, {}'.format(self.__nombre, self.__CiudadNatal, self.__PaisOrigen, self.__DNI)
    
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return '{}'.format(self.__DNI)