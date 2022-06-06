from manejadorEquipos import arregloNumPy

from ManejadorJugadores import manejadorJugadores

from ManejadorContrato import arregloNumPy as an2

def menu():
    print('Menu De opciones')
    print('1- Crear un contrato para un jugador en un equipo')
    print('2- Consultar jugadores contratados ')
    print('3- Consultar contratos ')
    print('4- Obtener importe de los contratos')
    print('5- Guardar  contratos ')
    print('0- Salir ')
    band= False 
    
    while not band :
        opcion=int(input("Ingrese la opcion:   "))
        if opcion in [1,2,3,4,5,0]:
            band=True
        return opcion  
    
    
    
    
if __name__=='__main__':
    
    arregloEquipo=arregloNumPy(10)
    arregloEquipo.testEquipo()
    #arregloEquipo.mostrarDatos()
    mj=manejadorJugadores()
    mj.testJugador()
    #mj.mostrarDatos()
    mc=an2(5)
    
    
    opcion= menu()
    
    while opcion!=0:
        if opcion==1:
            j=input("Ingrese el DNI del jugador quien se esta contratando  \n")
            print(j)
            jugador=mj.getJugador(j)
            e=str(input('Ingrese el nombre del equipo que lo contratara \n'))
            equipo=arregloEquipo.getEquipo(e)
            mc.testContrato(equipo, jugador)
            
            
            mc.mostrarDatos()
            
            pass
        elif opcion==2:
            pass
        elif opcion==3:
            pass
        elif opcion==4:
            pass 
        elif opcion==5:
            pass
        opcion=menu()
    

