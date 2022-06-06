import json

from pathlib import Path

from claseAparatosElectronicos import AparatosElectronicos


class Lavarropa(AparatosElectronicos):
    __capacidad=00
    __velocidadCentrifugado=00
    __programas=00
    __tipoCarga=""

    def __init__(self, marca, modelo, color, pais, preciobase, capacidad, velocidad, programas, tipoCarga):
        super().__init__(marca, modelo, color, pais, preciobase)
        self.__capacidad=capacidad
        self.__velocidadCentrifugado=velocidad
        self.__programas=programas
        self.__tipoCarga=tipoCarga



    def getImporteVenta(self):

        impVenta=0
        if self.__capacidad<=5:
            impVenta=self.__prcioBase*1.01
        elif self.__capacidad>5:
            impVenta=self.__prcioBase*1.03
        
        return impVenta

    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(

            )
        )
        return d

    
