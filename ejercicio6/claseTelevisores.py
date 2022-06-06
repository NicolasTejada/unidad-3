import json

from pathlib import Path

from claseAparatosElectronicos import AparatosElectronicos


class Televisores(AparatosElectronicos):
    __pantalla=""
    __pulgadas=""
    __definicion=""
    __conexionInternet=False

    def __init__(self, marca, modelo, color, pais, preciobase, tipoPantalla, pulgadas, definicion, conexionInternet=False):
        super().__init__(marca, modelo, color, pais, preciobase)
        self.__pantalla=tipoPantalla
        self.__pulgadas=pulgadas
        self.__definicion=definicion 
        self.__conexionInternet=conexionInternet


    def getImporteVenta(self):

        impVenta=0
        if self.__conexionInternet==True:
                
                if self.__definicion=='sd':
                    impVenta=self.__prcioBase*1.11
                elif self.__definicion=='hd':
                    impVenta=self.__prcioBase*1.12
                elif self.__definicion=='fullhd':
                    impVenta=self.__prcioBase*1.13
        else:
            if self.__definicion=='sd':
                    impVenta=self.__prcioBase*1.01
            elif self.__definicion=='hd':
                    impVenta=self.__prcioBase*1.02
            elif self.__definicion=='fullhd':
                    impVenta=self.__prcioBase*1.03
        
        return impVenta


    
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(

            )
        )
        return d
        