import json

from pathlib import Path

from claseAparatosElectronicos import AparatosElectronicos


class Heladera(AparatosElectronicos):
    __capacidad=''
    __freezer=False
    __ciclica=False

    def __init__(self, marca, modelo, color, pais, preciobase, capacidad, freezer= False, ciclica=False):
        super().__init__(marca, modelo, color, pais, preciobase)
        self.__capacidad=capacidad
        self.__freezer=freezer
        self.__ciclica=ciclica


    def getImporteVenta(self):
        impVenta=0
        if self.__ciclica==True:
                if self.__freezer==False:
                    impVenta=self.__prcioBase*1.11
                elif self.__capacidad>5:
                    impVenta=self.__prcioBase*1.13
        else:
            if self.__freezer==False:
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