


contaCasos = 0
opt = 1
listaLados = []
flag = 1
while opt >= 1:
    lado = int(input('Dame el lado del triangulo: '))
    if lado > 0:
        listaLados.append(lado)
        contaCasos = contaCasos + 1
    else:
        if contaCasos <= 0:
            print('No se ingresaron casos de prueba')
            flag = 0
        opt=0    

matDatos = []    

for j in range(len(listaLados)):
    aux = []
    lado = listaLados[j]
    suma = 0
    for i in range(lado):
        suma = suma + ((i+1)*3)
    #print(suma)
    aux.append(lado)
    aux.append(suma)

    matDatos.append(aux)





#print(matDatos)
print("\n")
for fila in matDatos:
    print(f'Para formar un triangulo de lado {fila[0]} se necesitan  {fila[1]} palos de fosforos.')

print("\n")

sumParPar = 0
sumImpImp = 0
sumImpPar = 0
sumParImp = 0

for fila in matDatos:
    #lado par , palos de fosforo par
    if fila[0] % 2 == 0 and fila[1] % 2 == 0:
        #print("Lado par,fosforo par",fila)
        sumParPar = sumParPar + 1
    #lado impar , palos de fosforo impar
    elif fila[0] % 2 !=0  and fila[1] % 2 != 0:
        #print("Lado impar,fosforo impar",fila)
        sumImpImp = sumImpImp + 1
    #lado impar,palos de fosforo par
    elif fila[0] % 2 != 0 and fila[1] % 2 == 0:
        #print("Lado impar,fosforos par",fila)
        sumImpPar = sumImpPar + 1
    elif fila[0] % 2 == 0 and fila[1] % 2 != 0:
        #print("Lado par,fosforos imapar",fila)
        sumParImp = sumParImp + 1

print("\n")

if flag == 1:
    print("REPORTE FINAL")
    print("=============")
    print("\n")

    print(f"Total casos de prueba procesados:{contaCasos}")
    print(f"Total casos de prueba altura par que requiere cantidad par de fosforos= {sumParPar} ")
    print(f"Total casos de prueba altura impar que requiere cantidad impar de fosforos= {sumImpImp} ")
    print(f"Total casos de prueba altura impar que requiere cantidad par de fosforos= {sumImpPar} ")
    print(f"Total casos de prueba altura par que requiere cantidad impar de fosforos= {sumParImp} ")

#sumParPar 
#sumImpImp
#sumImpPar
#sumParImp
