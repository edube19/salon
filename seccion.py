#creando la sección de clases

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
from asyncio.windows_events import NULL
from distutils.log import info



info_alumnos=[[],[],[]]#[[alumnos],[notas],[nota final],[identificador_alumno]]
notas_max_min=[[]]#[alumno][1]→ nota menor,[alumno][0]→ nota mayor .Lista de la mejor/menor nota de cada alumno
notas_min_pc=[]#la pc mas baja de cada alumno
lista_nombres=[]#guarda los nombres de todos los alumnos
class Seccion:
    def __init__(self,nseccion,curso,profesor):
        self.nseccion=nseccion
        self.curso=curso
        self.profesor=profesor
    #lista_alumnos=[]

    def agregar_alumno(self,info_alumnos,curso,nseccion):
        cond=1
        while(cond!=0):
            nombre_valido=0#si es cero seguira pidiendo el nombre
            while(nombre_valido==0):
                nombreAlumno=input("Nombre del alumno a ingresar: ")
                if nombreAlumno.isalpha():
                    nombre_valido=1#se ingreso un nombre valido (solo letras)
                else:
                    print("Ingrese solo nombres")
            if nombreAlumno in lista_nombres:
                print("Ya existe este alumno")
            else:
                lista_nombres.append(nombreAlumno)
                info_alumnos[0].append(Alumno(nombreAlumno,nseccion,curso))#poner al final en la lista de alumnos
                print("Se agrego al alumno: "+nombreAlumno)
            cond=int(input("Desea agregar otro alumno (1→SI / 0→NO):"))

    def quitar_alumno(self,info_alumnos):
        cond=1
        while(cond!=0):
            nombreAlumno=input("Nombre del alumno a eliminar: ")
            if nombreAlumno in info_alumnos[0]:
                info_alumnos[0].remove(nombreAlumno)
                print("Se elimino al alumno: "+nombreAlumno)
            else:
                print("Ya no existe ese alumno")
            cond=input("Desea eiminar otro alumno (1→SI / 0→NO):")
            if cond==0:
                break

    def ver_lista(self,info_alumnos,nseccion):
        print("Lista de alumnos de la seccion "+str(nseccion)+": ")
        for x in range(len(info_alumnos[0])):
            print("Alumno n° "+str(x+1)+" : "+info_alumnos[0][x].nombre)
        return len(info_alumnos[0])

    def mayor_nota(self,info_alumnos):
        vacio=[]
        max_value = 0
        max_idx = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio):
                if (max_value ==0 or num > max_value):
                    max_value = num
                    max_idx = idx
        print('La Maxima nota es: ', str(max_value), "del alumno: ", str(info_alumnos[0][max_idx].nombre))

        tres_mejores_notas=[]
        tres_mejores_notas.append(max_value)
        print("..................")
        print(tres_mejores_notas)

        vacio=[]
        max_value1 = 0
        max_idx1 = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio and info_alumnos[2][idx] not in tres_mejores_notas):
                if (max_value1 < max_value or num > max_value1 ):
                    max_value1 = num
                    max_idx1 = idx
        tres_mejores_notas.append(max_value1)

        vacio=[]
        max_value2 = 0
        max_idx2 = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio and info_alumnos[2][idx] not in tres_mejores_notas):
                if (max_value2 < max_value1 or num > max_value2 ):
                    max_value2 = num
                    max_idx2 = idx
        print("Las tres mejores notas son: ")
        print("3 mejor nota es: "+str(max_value2)+" del alumno: "+str(info_alumnos[0][max_idx2].nombre))
        print("2 mejor nota es: "+str(max_value1)+" del alumno: "+str(info_alumnos[0][max_idx1].nombre))
        print("La mejor nota es: "+str(max_value)+" del alumno: "+str(info_alumnos[0][max_idx].nombre))

    def menor_nota(self,info_alumnos):   
        vacio=[]
        min_value = 20
        min_idx = None
        for idx, num in enumerate(info_alumnos[2]):
            if (info_alumnos[2][idx]!=vacio):
                if (min_value == 20 or num < min_value ):
                    min_value = num
                    min_idx = idx
        print('La menor nota es: ', str(min_value), "del alumno: ", str(info_alumnos[0][min_idx].nombre))
    def recibir_notas(self,info_alumnos,alumno):
        notas=[]#aca se guardaran las notas
        vacio=[]
        contador=0
        validacion_nota=0
        notascero=[]#solo para inicializar las notas
        for j in range(6):
            notas.append(notascero)
        # print(notas)
        while (contador!=len(info_alumnos[0])):
            if alumno in info_alumnos[0][contador].nombre:
                if(info_alumnos[1][contador]==vacio):
                    print("Ingresar notas del alumno "+info_alumnos[0][contador].nombre+": ")    
                    for k in range(6):
                        if k<4:
                            while(validacion_nota==0):
                                notas[k]=int(input(f'PC{str(k+1)}: '))
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                            validacion_nota=0
                        elif k==4:
                            while(validacion_nota==0):
                                notas[k]=int(input("Parcial: "))
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                            validacion_nota=0
                        else:
                            while(validacion_nota==0):
                                notas[k]=int(input("Final: "))
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                    print(notas)
                    contador=len(info_alumnos[0])
                else:
                    print("Las notas del alumno "+alumno+" ya fueron ingresadas")
                    print(info_alumnos[1][contador])  
                    contador=len(info_alumnos[0])
            else:
                contador=contador+1
                if (contador==len(info_alumnos[0])):
                    print("No existe el alumno")
                

    def ver_notas(self,info_alumnos,nombre):
        for j in range(len(info_alumnos[0])):
            if nombre==info_alumnos[0][j].nombre:
                print("Notas del alumno "+nombre+" : ")
                print(info_alumnos[1][j])
                break
            elif (j==(len(info_alumnos[0])-1)):
                print("No esta el alumno "+nombre)

    def ver_notas_seccion(self,info_alumnos,seccion):
        print("Notas de la sección "+str(seccion))
        print(info_alumnos[1])

    def inicializar_notas(self,columna):    #inicializando las notas para que haya listas vacias en la columna notas (sino marca error)
        for j in range(len(info_alumnos[0])):
            notas=[]
            info_alumnos[columna].append(notas)

    def inicializar_notas_min_pc(self,notas_min_pc):

        for j in range(len(info_alumnos[0])):
                notas=[]
                notas_min_pc.append(notas)


    def promedio_alumnos(self,info_alumnos,notas_min_pc):
        #minimo=min(info_alumnos)
        #menor=20
        min_valor=[]
        vacio=[]
        for i in range(len(info_alumnos[0])):
            if info_alumnos[1][i]!=vacio:
                for j in range(4):#lee las 4 primeras notas
                    a=info_alumnos[1][i][j]
                    min_valor.append(a)
                menor=min(min_valor)
                notas_min_pc[i]=menor
                min_valor=[]
        
        #poniendo las notas finales de cada alumno
        notapcs=0
        for x in range(len(info_alumnos[0])):  
            if info_alumnos[1][x]!=vacio:
                for j in range(4):
                    if info_alumnos[1][x][j]==notas_min_pc[x]:#no lee la nota menor
                        notapcs=notapcs
                    else:
                        notapcs=info_alumnos[1][x][j]+notapcs
                notapcs=notapcs/3
                info_alumnos[2][x]=(notapcs+info_alumnos[1][x][4]+info_alumnos[1][x][5])/3#alumnos[1][x][4]→parcial, alumnos[1][x][5]→final
                print("Promedio final del alumno "+str(info_alumnos[0][x].nombre)+" es: "+str(info_alumnos[2][x]))
                notapcs=0

class Alumno:
    def __init__(self,nombre,nseccion,curso):
            self.nombre=nombre
            self.nseccion=nseccion
            self.curso=curso


class Notas:
    #info_alumnos[0][n]= Alumno(nombreAlumno,nseccion,curso)
    #info_alumnos[1][n]= Alumno(nombreAlumno,nseccion,curso)
    def __init__(self,alumno):
        self.alumno=alumno
    
    

    
                
       
