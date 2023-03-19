#importamos la librería
import numpy as np


asientosAvion = np.zeros(shape=(7,6), dtype='int')
referenciaCoordenadas = np.zeros(shape=(7,6), dtype='int')


listaPasajero = []





def numerarAsientos():
    fila = asientosAvion.shape[0] 
    col = asientosAvion.shape[1] 
    asientos = 1 
    for filas in range(fila):
        for columnas in range(col):
            asientosAvion[filas][columnas] = asientos
            asientos = asientos + 1

def numerarReferencia():
    fila = referenciaCoordenadas.shape[0] 
    col = referenciaCoordenadas.shape[1] 
    asientos = 1 
    for filas in range(fila):
        for columnas in range(col):
            referenciaCoordenadas[filas][columnas] = asientos
            asientos = asientos + 1



def mostrarAsientos():
    f = asientosAvion.shape[0] 
    c = asientosAvion.shape[1] 
    print("")
    for fila in range(f):
        for columna in range(c):
            #print(str(asientosAvion[fila][columna]),end='\t')
            if columna == 0:
                print('| '+str(asientosAvion[fila][columna]),end='\t')
            elif columna == 2:
                print(asientosAvion[fila][columna] , end='\t\t')
            elif columna == 5:
                print(str(asientosAvion[fila][columna]) + ' |',end='\t')
            else:
                print(str(asientosAvion[fila][columna]),end='\t')     
        
            
        print(" ")
        print("|                                                  |")  
        if fila == 4:
            print('|-----------------              -------------------|')
            print('|-----------------              -------------------|')
               


def anularVuelo():
    numero_asiento = 0
    while numero_asiento<1 or numero_asiento>42:
      #valida el rango de asientos
      numero_asiento = int(input("Numero de asiento a Anular: "))
    
    
    fila_buscada = np.where(referenciaCoordenadas==numero_asiento)[0][0]
    columna_buscada = np.where(referenciaCoordenadas==numero_asiento)[1][0]
    if asientosAvion[fila_buscada][columna_buscada] == 0: 
        asientosAvion[fila_buscada][columna_buscada] = numero_asiento
        listaPasajero.clear()
        print (f'Se a anulado el asiento Nº {numero_asiento} ')

    else:
        print("Este asiento esta libre y no se puede anular")


def modificar():
    nAsiento = int(input('Ingrese el Numero de Asiento: '))
    rut = input('Ingrese el RUT: ')

    #if rut == listaPasajero[1] and nAsiento == listaPasajero[5]:
    try:
        if rut == listaPasajero[1] and nAsiento == listaPasajero[5]:
            print("")
            print(f'1-Nombre: {listaPasajero[0]}')
            print(f'2-Telefono: {listaPasajero[2]}')
            print(f'3-Nombre y telefono')
            opt = input('Cual dato desea modificar?: ')

            if opt == '1':
                nombre = input('Ingrese el Nombre: ')
                listaPasajero[0] = nombre 
            elif opt == '2':
                telefono = input('Ingrese el Telefono: ')
                listaPasajero[2] = telefono
            elif opt == '3':
                nombre = input('Ingrese el Nombre: ')
                telefono = input('Ingrese el Telefono: ')
                listaPasajero[0] = nombre
                listaPasajero[2] = telefono
            print("")
            print("Se an modificado los datos con exito:")
            print(f'1-Nombre: {listaPasajero[0]}')
            print(f'2-Telefono: {listaPasajero[2]}')

    except:
        print("Lista nula")
        


numerarAsientos()
numerarReferencia()







while True:
    print("")
    print("MENU")
    print("=====\n")
    print("1-Ver asientos Disponibles")
    print("2-Comprar Asiento")
    print("3-Anular Vuelo")
    print("4-Modificar datos Pasajero")
    print("5-Salir")

    opt = input('Ingrese su Opcion: ')
   
    if opt == '1':
        print("")
        print("Ver Asientos Disponibles")
        print('------------------------\n')
    
        mostrarAsientos()
    if opt == '2':
        print("")
        print("Comprar Asiento Disponible")
        print('---------------------------\n')
        listaPasajero.clear()
        nom = input('Ingrese el nombre del pasajero: ')
        rut = input('Ingrese el RUT del pasajero: ')
        telef = input('Ingrese el telefono del pasajero: ')
        edad = input('Ingrese la edad del pasajero: ')
        banco = input('¿El Pasajero es usuario del Banco Douc? s/n : ')
        
        listaPasajero.append(nom)
        listaPasajero.append(rut)
        listaPasajero.append(telef)
        listaPasajero.append(edad)
        listaPasajero.append(banco)


        optAsiento = 'n'
        while optAsiento == 'n':
        
            #Comprar los asientos
            numero_asiento = 0
            valorAsieno = 0
            while numero_asiento<1 or numero_asiento>42:
            #valida el rango de asientos
                numero_asiento = int(input("Numero de asiento a comprar: "))

            #este código asegura que si el asiento está vacío, no se pueda comprar
            try:
                fila_buscada = np.where(asientosAvion==numero_asiento)[0][0]
                columna_buscada = np.where(asientosAvion==numero_asiento)[1][0]
                
                if numero_asiento >=1 and numero_asiento <=30:
                    optAsiento = input('A elegido un asiento normal el cual tiene un valor de $67800,desea comprarlo? s/n: ')
                    valorAsiento = 67800
                
                if numero_asiento >=31 and numero_asiento <=42:
                    optAsiento = input('A elegido un asiento VIP el cual tiene un valor de $140500,desea comprarlo? s/n: ')
                    valorAsiento = 140500

            except:
                print('El asiento está ocupado') 
                
            
        asientosAvion[fila_buscada][columna_buscada] = 0
        
        print("")
        
        if listaPasajero[4] == 's':
            valorAsiento = valorAsiento - (valorAsiento * 0.15)
            print("Se le a hecho un descuento del 15% por ser usuario del Banco Duoc")

        listaPasajero.append(numero_asiento)
        listaPasajero.append(valorAsiento)
        print(f'Usted ha comprado el asiento Nº{numero_asiento} con un valor de ${valorAsiento}')
        

            

    if opt == '3':
        print("")
        print("Anular Vuelo")
        print("-------------\n")
        
        anularVuelo()
    if opt == '4':
        print("")
        print("Modificar Datos Pasajero")
        print("------------------------\n")

        modificar() 
    if opt == '5':
        break 