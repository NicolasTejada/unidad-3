from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __PotenciaMaxima=00
    
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__PotenciaMaxima=potencia
        
    
    def __str__(self):
        return 'Modelo{} Marca{} potencia{}'.format(super().getModelo, super().getMarca, self.__PotenciaMaxima)