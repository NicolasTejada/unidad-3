from ManejadorFlores import arregloNumPy



def Menu():
    print('Menu Opciones:     ')
    print('-------------------------------')
    print('1- Registrar un ramo vendido')
    print('2- Lista de las cinco flores mas pedidas')
    print('3- Flores vendidas segun el tamaño del ramo')
    print('0- Salir del menu')
    bandera=False
    while not bandera:
        opcion=int(input('Seleccione una opcion: '))
        if opcion in [1,2,3]:
            bandera=True
        elif opcion==0:
            print('good bye\n')
            bandera=True
    return opcion 

def SMenu():
    print('Seleccione el tamaño del ramo')
    print('1- chico')
    print('2- mediano')
    print('3- grande')
    opcion=int(input('Ingrese la opcion '))
    return opcion
   
    
    
    
if __name__=='__main__':
    
    arregloFlores=arregloNumPy(4)
    arregloFlores.testFlores()
    
    arregloFlores.Mostrardatos()

    opc=Menu()
    while opc!=0:
        
        if opc==1:
            
            opcion=SMenu()
            
            if opcion==1:
                pass
                '''
                tamaño='chico'
                unRamo=Ramo(tamaño)
                arregloFlores.agregarRamo(unRamo)
                for i in range(3):
                    f=input('Ingrese el nombre de la flor a agregar en el ramo')
                    
                    unRamo.addFlor()
                  '''  
            elif opcion==2:
                tamaño='mediano'
            elif opcion==3:
                tamaño='Grande'
            
        elif opc==2:
            pass
        
        elif opc==3:
            pass
        
        opc=Menu()
        
        
        
        
    
        
        