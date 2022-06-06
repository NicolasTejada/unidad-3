class Equipo:
    Nombre=""
    Ciudad=""
    
    def __init__(self, nombre, ciudad):
        self.Nombre=nombre
        self.Ciudad=ciudad
        
    def __str__(self):
        return '{}{}'.format(self.Nombre, self.Ciudad)
    
    
    def getNombre(self):
        
        return self.__Nombre
    
    
    
        
        