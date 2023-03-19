import os
from datetime import datetime



def letrero():
	
	print('')
	print("******************************************")
	print("*  Servicio De Atencion Medica Urgencias *")
	print("******************************************")

def menu():
	os.system('cls')
	letrero()
	print('')
	print('MENU')
	print ('')
	print(' 1) Ingresar Ficha del Paciente')
	print(' 2) Buscar Ficha por Rut')
	print(' 3) Buscar Medicamentos por Rut')
	print(' 4) Eliminar Ficha del Paciente')
	print(' 5) Listar Pacientes Atendidos')
	print(' 6) Salir')
	print('')



	 


def ingresarFicha(cont):
	vecDatos = []
	vecMedicamentos = []
	numFichaIngreso = ''
	fechAtencion = ''
	horaAtencion = ''
	nomPersonal = ''

#---------------------------
#identificacion del paciente		
	
	nombre = ''
	apellido = ''
	nivelUrgencia = ''
	rut = ''
	sexo = ''
	estCivil = ''
	edad = ''
	domicilio = ''
	grupoSanguineo = ''
	fono = ''
	asisteAcompaniado = ''

#identificacion acompañante	
	nombreAcom = ''
	apeAcom = ''
	rutAcom = ''
	gradoParentesco = ''
	fonoAcom = ''

#motivo consulta medica
	descripPaciente = ''

#-----------------------------------------------
#informacion de atencion
	nomMedico = ''
	especialidad = ''
	sintomasDetectados = ''
	diagnostico = ''
	reposo = ''
	cantDiasRep = ''

#--------------------------------------------
#info medicamento			

	asignaMed = ''
	nomMedicamento = ''
	dosis = ''
	cantDias = ''

	os.system('cls')
	letrero()
	print('')
	print ('1-Ingresar Ficha del Paciente')
	print ('')
	
	ahora = datetime.now()
	
	numFichaIngreso = cont
	fechAtencion = str(ahora.day) + '/' + str(ahora.month) + '/' + str(ahora.year) 
	horaAtencion = str(ahora.hour) + ':' + str(ahora.minute) + ':' + str(ahora.second)
	
	nomPersonal = input('>Ingrese el nombre de la Persona a cargo: ')
	print ('')
	nombre = input('>Ingrese el nombre del paciente: ')
	apellido = input('>Ingrese el apellido del paciente: ')
	nivelUrgencia = input('>Ingrese el nivel de urgencia: ')
	
	
	
	#valida que el rut no este vasio
	#cicla hasta que se ponga el rut
	opt = True
	while opt:
		rut = input('Ingresa el RUT del Paciente: ')
		opt = validaRutVacio(rut)
	
	sexo = input('>Ingrese el sexo del paciente: ')
	estCivil = input('>Ingrese el estado civil del paciente: ')
	edad = input('>Ingrese la edad del paciente: ')
	domicilio = input('>Ingrese el domicilio del paciente: ')
	grupoSanguineo = input('>Ingrese el Grupo Sanguineo del paciente: ')
	fono = input('>Ingrese el fono del paciente: ')
	asisteAcompaniado = input('>El paciente Ingreso acompañado? (s/n): ')
	if asisteAcompaniado == 's':
		print('')
		nombreAcom = input('>Ingrese el nombre del Acompañante: ')
		apeAcom = input('>Ingrese el apellido del Acompañante: ')
		rutAcom = input('>Ingrese el Rut del acompañante: ')
		gradoParentesco = input('>Ingrese el grado de parentesco: ')
		fonoAcom = input('>Ingrese el fono del acompañante: ')
		print('')
	
	descripPaciente = input('>Ingrese la descripcion del paciente: ')
	print('')
	nomMedico = input('>Ingrese el Nombre del Medico: ') 
	especialidad = input('>Ingrese la especialidad: ')
	sintomasDetectados = input('>Ingrese los sintomas detectados: ')
	diagnostico = input('>Ingrese el diagnostico: ')
	reposo = input('>El paciente tiene reposo? (s/n): ')
	if reposo == 's':
		cantDiasRep = input('>Ingrese los dias de reposo: ')
	print ('')

	asignaMed = input('>Medico Asigna Medicamento?(s/n): ')

	if asignaMed == 's':
		opt = 's'
		while opt == 's':
			nomMedicamento = input('>Ingrese el nombre del medicamento: ')
			dosis = input('>Ingrese la dosis: ')
			cantDias = input('>Ingrese la cantidad de dias: ')
			vecMedicamentos.append(nomMedicamento)
			vecMedicamentos.append(dosis)
			vecMedicamentos.append(cantDias)
			opt = input('>Agregar otro Medicamento (s/n): ')




	vecDatos.append(str(numFichaIngreso))
	vecDatos.append(fechAtencion)
	vecDatos.append(horaAtencion)
	vecDatos.append(nomPersonal)
	vecDatos.append(nombre)
	vecDatos.append(apellido)
	vecDatos.append(nivelUrgencia)
	vecDatos.append(rut)
	vecDatos.append(sexo)
	vecDatos.append(estCivil)
	vecDatos.append(edad)
	vecDatos.append(domicilio)
	vecDatos.append(grupoSanguineo)
	vecDatos.append(fono)
	vecDatos.append(asisteAcompaniado)
	vecDatos.append(nombreAcom)
	vecDatos.append(apeAcom)
	vecDatos.append(rutAcom)
	vecDatos.append(gradoParentesco)
	vecDatos.append(fonoAcom)
	vecDatos.append(descripPaciente)
	vecDatos.append(nomMedico)
	vecDatos.append(especialidad)
	vecDatos.append(sintomasDetectados)
	vecDatos.append(diagnostico)
	vecDatos.append(reposo)
	vecDatos.append(cantDiasRep)
	vecDatos.append(asignaMed)
	vecDatos.append(vecMedicamentos)
	
	matFichas.append(vecDatos)


	#print (vecDatos)
	#print(matFichas)
	print('')
	input('Datos Gravados,Precione Enter Para continuar...')

def buscarFicha():
	if validarMatVasia(matFichas):
		os.system('cls')
		letrero()
		print('')
		print ('2-Buscar Ficha Por Rut')
		print ('')
		opt = True
		while opt:
			rutPac = input('Ingresa el RUT del Paciente: ')
			opt = validaRutVacio(rutPac)
		print('')		 		
		
		existe = False	
		for i in range(len(matFichas)):
			if matFichas[i][7] == rutPac:
				matrizFicha = matFichas[i]
				existe = True
				ficha(matrizFicha)
				break
				
		if not existe:
			print('No existe el RUT')
		input('Precione Enter para volver al Menu Principal...')
	else:
		print('No hay ninguna Ficha disponible.')
		input('Precione  Enter para continuar...')	

def buscarMedicamento():
	if validarMatVasia(matFichas):
		os.system('cls')
		letrero()
		print('')
		print ('3-Buscar Medicamento Por Rut')
		print('')

		opt = True
		while opt:
			rutPac = input('Ingresa el RUT del Paciente: ')
			opt = validaRutVacio(rutPac)
		print('')		
		print ('Remedios Recetados')
		print ('------------------') 		
		
		existe = False	
		for i in range(len(matFichas)):
			if matFichas[i][7] == rutPac:
				remedios = matFichas[i][28]
				existe = True
				for j in range(0,len(remedios),3):
					print ('-' + remedios[j])
				break	
		if not existe:
			print('No existe el RUT')
							
		
		print ('')
		input('Precione Enter para volver al menu Principal...')
	else:
		print('No hay ninguna Ficha disponible.')
		input('Precione  Enter para continuar...')

def eliminarFicha():
	if validarMatVasia(matFichas):
		os.system('cls')
		letrero()
		print('')
		print ('4-Eliminar Ficha')
		print ('')
		opt = True
		while opt:
			rutPac = input('Ingresa el RUT del Paciente a eliminar: ')
			opt = validaRutVacio(rutPac)
		print('')		 		
		
		existe = False	
		for i in range(len(matFichas)):
			if matFichas[i][7] == rutPac:
				existe = True
				borar = input('Seguro quiere borra esta ficha? (Ingresar s para borrar/otra tecla para salir): ')
				if borar == 's':
					del(matFichas[i])
					print('Se a Boorado la Ficha. ')
				else:
					print ('No se a borrado la Ficha')	
				print('')
				
				break
				
				
		if not existe:
			print('No existe el RUT')
		input('Precione Enter para volver al Menu Principal...')
	else:
		print('No hay ninguna Ficha disponible.')
		input('Precione  Enter para continuar...')

def listarPacientes():
	if validarMatVasia(matFichas):
		os.system('cls')
		letrero()
		print('')
		print ('5-Lista de Pacientes')
		print ('')
		print('RUT              Nombre                  Apellido')
		print('------           ------                  --------')
		for i in range(len(matFichas)):
			print (matFichas[i][7] + '       ' + matFichas[i][4] + '                  ' + matFichas[i][5])
		print('')
		input('Precione enter para volver al Menu principal...')
	else:
		print('No hay ninguna Ficha disponible.')
		input('Precione  Enter para continuar...')

def ficha(matriz):
	print ('')
	print ('---------------Servicio De Salud Empire---------------') 
	print ('                Unidad de Urgencias                   ')
	print ('')
	print ('                FICHA DE INGRESO N {0}                  '.format(matriz[0]))
	print('')
	print('Fecha de Atencion: {0}              Hora de Atencion: {1}  '.format(matriz[1],matriz[2]))
	print('')
	print ('Nombre del Personal que ingresa la ficha: {0}'.format(matriz[3]))
	print ('')
	print('')
	print('IDENTIFICACION DEL PACIENTE')
	print('')
	print('Nombre: {0}                        Apellido: {1}'.format(matriz[4],matriz[5]))
	print('')
	print('Nivel de Urgencia: {0}'.format(matriz[6]))
	print('')
	print('Rut: {0}                            Sexo: {1}'.format(matriz[7],matriz[8]))
	print('')
	print('Estado Civil: {0}                    Edad: {1} '.format(matriz[9],matriz[10]))
	print('')
	print('Domicilio: {0}                       Grupo Sanguineo: {1}'.format(matriz[11],matriz[12]))
	print('')
	print('Fono: {0}'.format(matriz[13]))
	print('')
	print('Asiste Acompañado: {0}'.format(matriz[14]))
	print('')
	print('')
	print('IDENTIFICACION DE ACOMPAÑANTE')
	print('')
	print('Nombre: {0}                         Apellido: {1}'.format(matriz[15],matriz[16]))
	print('')
	print('Rut: {0}'.format(matriz[17]))
	print('')
	print('Grado de Parentesgo: {0}            Fono: {1}'.format(matriz[18],matriz[19]))
	print('')
	print('')
	print('MOTIVO DE CONSULTA MEDICA')
	print('')
	print('Descripcion Del Paciente: {0}'.format(matriz[20]))
	print('')
	print('')
	print('INFORMACION DE ATENCION')
	print('')
	print('Nombre Medico: {0}'.format(matriz[21]))
	print('')
	print('Especialidad: {0}'.format(matriz[22]))
	print('')
	print('Sintomas Detectados: {0}'.format(matriz[23]))
	print('')
	print('Diagnostico: {0}'.format(matriz[24]))
	print('')
	print('Reposo: {}'.format(matriz[25]))
	print('')
	print('Cantidad de Dias: {0}'.format(matriz[26]))
	print ('')
	print('')
	print ('INFORMACION DE MEDICAMENTO')
	print('')
	print('Medico asigna Mesicamento: {0}'.format(matriz[27]))
	print('')

	
	for i in range(len(matriz[28])):
		if i % 3 == 0:
			print ('Nombre Medicamento: {0}'.format(matriz[28][i]))
			print('Dosis: {0}'.format(matriz[28][i-2]))
			print ('Cantidad de dias: {0} '.format(matriz[28][i-1]))
			print ()
#----------------------------------------------------------------------
def validarMatVasia(contenido):
	if len(contenido) != 0:
		return True
	else:
		return False

def validaRutVacio(ruut):
	sacarSaltodeLinea = ruut.rstrip('\n')
	if len(sacarSaltodeLinea) != 0:
		return False
	else: 
		return True				
		








if __name__ == '__main__':
	 	matFichas = []
	 	
	
	 	contaFicha = 0
	 	while True:
	 		menu()
	 		opcion = input('Elija una Opcion: ')
	 		if opcion == '1':
	 			ingresarFicha(contaFicha)
	 			contaFicha = contaFicha + 1 
	 			



	 		elif opcion == '2':
	 			buscarFicha()

	 		elif opcion == '3':
	 			buscarMedicamento()
	 			
	 		elif opcion == '4':
	 			eliminarFicha()
	 			
	 		elif opcion == '5':
	 			listarPacientes()
	 			
	 		elif opcion == '6':
	 			print ('Ejecucion del programa terminada,Gracias por usar este Software')
	 			break					



	 		 