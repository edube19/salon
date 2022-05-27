from re import X


dic = {}
i=0
#Agregar Nombre
while True:
    print('Ingresar todos los alumnos inscritos')
    opcion = str(input('Agregar Alumno SI(S) o NO(N): '))
    if(opcion == 'S' or opcion == 's'):
        i+=1
        dic[i] = {}
        nombre = str(input('Nombre: '))
        dic[i]['Nombre'] = nombre
        opcion_seccion = str(input('Ingrese la seccion del alumno ' + dic[i]['Nombre'] +': '))
        dic[i]['Seccion'] = opcion_seccion
    else:
        break

#Agregar notas a los ALUMNOS
for j in dic.keys():
    print("\n----------------------------")
    print('Vamos a ingresar las NOTAS de ',dic[j]['Nombre'])
    dic[j]['PCs']=[]
    dic[j]['Examenes']=[]
    for k in range(4):
        nota_pc = int(input(f'Ingrese la PC{k+1}: '))
        dic[j]['PCs'].append(nota_pc)
    nota_parcial = int(input('Ingrese la nota del PARCIAL: '))
    dic[j]['Examenes'].append(nota_parcial)
    nota_final = int(input('Ingrese la nota del FINAL: '))
    dic[j]['Examenes'].append(nota_final)
    #Obtenemos el promedio de PCs
    promedio_pc = 0
    for pc in dic[j]['PCs']:
        promedio_pc += pc
    promedio_pc = (promedio_pc - min(dic[j]['PCs']))/3
    promedio_final = (promedio_pc + dic[j]['Examenes'][0] + dic[j]['Examenes'][1])/3
    print(promedio_final)

print(dic)

#VER ALUMNOS POR SECCION
print('\nIMPRIMIENDO ALUMNOS SOLO DE LA SECCION V')
for l in dic.keys():
    if dic[l]['Seccion'] == 'V':
        print(dic[l]['Nombre'])

""" dic['1'] = {}
dic['1']['Nombre'] = "Angel"
dic['1']['PCs'] = [15,16,14,15]
dic['1']['Examenes'] = [13,14]

dic['2'] = {}
dic['2']['Nombre'] = "Jean"
dic['2']['PCs'] = [13,18,13,11]
dic['2']['Examenes'] = [15,12] """

""" for i in dic.keys():
	# print(dic[i]['Nombre'])
    print(dic[i]['Nombre'])
    practicas = dic[i]['PCs']
    mas_bajo = min(practicas)
    Promedio = 0
    for j in practicas:
        Promedio += j
    Promedio = (Promedio-mas_bajo)/(len(practicas)-1)
    print(practicas)
    print('Promedio de practicas',Promedio)
    print(dic[i]['Examenes'])
    Examenes = dic[i]['Examenes']
    PromedioFinal = (Promedio + Examenes[0] + Examenes[1])/3
    print('PROMEDIO FINAL', PromedioFinal)
print(dic) """