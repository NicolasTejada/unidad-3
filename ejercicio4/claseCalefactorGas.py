from claseCalefactor import Calefactor


class CalefactorGas(Calefactor):
    __Matricula=""
    __calorias=float 
    
    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.matricula=matricula
        self.__calorias= calorias
        
            
    def __str__(self):
        return 'Modelo {} Marca {} matricula {} Calorias {}'.format(super().getModelo, super().getMarca, self.__Matricula, self.__calorias)
    
    
    