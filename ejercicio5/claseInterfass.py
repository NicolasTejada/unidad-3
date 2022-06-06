from zope.interface import Interface
from zope.interface import implementer

class Interface(Interface):
    def InsertarElemento(coleccion, elem, posicion):
        try:
             coleccion[posicion]= elem
        except IndexError:
            print("La posicion ingresada no esta en el rango de la coleccion ")
           

      

    def agregarElemento(coleccion,elem):
        
        coleccion[len(coleccion)-1]=elem
        
    

    def mostrarElemento(coleccion, pocision):
        try:
           print(coleccion[pocision])

        except IndexError: 
            print("La posicion ingresada no esta en el rango de la coleccion ")
           

