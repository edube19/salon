#creando la sección de clases
from array import array
import numpy as np
#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
info_alumnos=np.array[[],[[]],[]]#[[alumnos],[notas],[nota final]]
notas_max_min=np.array[[],[]]#[alumno][1]→ nota menor,[alumno][0]→ nota mayor .Lista de la mejor/menor nota de cada alumno
notas_min_pc=np.array[[]]#la pc mas baja de cada alumno
class Seccion:
    def __init__(self,nseccion,curso,profesor):
        self.nseccion=nseccion
        self.curso=curso
        self.profesor=profesor
    #lista_alumnos=[]

    def agregar_alumno(self,info_alumnos,curso,nseccion):
        cond=1
        n=0
        while(cond!=0):
            nalumno=input("Nombre del alumno a ingresar: ")
            if nalumno in info_alumnos[0]:
                print("Ya existe ese alumno")
            #lista_alumnos.append(nalumno)
            else:    
                info_alumnos[0].append(nalumno)#poner al final en la lista de alumnos
                info_alumnos[0][n]= Alumno(nalumno,nseccion,curso)
                #info_alumnos[1][n]= Notas(nalumno)
                print("Se agrego al alumno: "+nalumno)
            n=n+1
            cond=input("Desea agregar otro alumno (1→SI / 0→NO):")
            cond=int(cond)
            """if cond==0:
                break"""
 
    def quitar_alumno(self,info_alumnos):
        cond=1
        while(cond!=0):
            nalumno=input("Nombre del alumno a eliminar: ")
            if nalumno in info_alumnos[0]:
                info_alumnos[0].remove(nalumno)
                print("Se elimino al alumno: "+nalumno)
            else:
                print("Ya no existe ese alumno")
            cond=input("Desea eiminar otro alumno (1→SI / 0→NO):")
            if cond==0:
                break

    def ver_lista(self,info_alumnos,nseccion):
        print("Lista de alumnos de la seccion "+str(nseccion)+": ")
        i=1
        for x in range(len(info_alumnos[0])):
            print("Alumno n° "+str(i)+" : "+str(info_alumnos[0][x].nombre))
            i=i+1

    def mayor_nota(self,info_alumnos):
        print("Mayor nota de la seccion")
        mayor=0
        for i in range(len(info_alumnos[2])):
            if info_alumnos[2][i]>mayor:
                mayor=info_alumnos[2][i]
                notas_max_min[0][i]=mayor
                j=i#guardamos la posicion del alumno con la mas alta nota
        print(mayor+" del alumno "+info_alumnos[0][j])

        print("Tres notas más altas de la seccion")
        mayor2=0
        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]>mayor2 and info_alumnos[2][i]<mayor):
                mayor2=info_alumnos[2][i]
                notas_max_min[0][i]=mayor2
                my2=i#guardamos la posicion del alumno con la mas alta nota
        
        mayor3=0
        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]>mayor3 and info_alumnos[2][i]<mayor and info_alumnos[2][i]<mayor2):
                mayor3=info_alumnos[2][i]
                notas_max_min[0][i]=mayor3
                my3=i#guardamos la posicion del alumno con la mas alta nota
        
        print(mayor+" del alumno "+info_alumnos[0][j])
        print(mayor2+" del alumno "+info_alumnos[0][my2])
        print(mayor3+" del alumno "+info_alumnos[0][my3])

        


    def menor_nota(self,info_alumnos):
        print("Menor nota de la seccion")
        menor=20
        for i in range(len(info_alumnos[2])):
            if info_alumnos[2][i]<menor:
                menor=info_alumnos[2][i]
                notas_max_min[1][i]=menor
                j=i#guardamos la posicon del alumno con la mas baja nota
        print(menor+" del alumno "+info_alumnos[0][j])
        
        print("Tres notas más altas de la seccion")
        menor2=20
        menor3=20

        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]<menor2 and info_alumnos[2][i]>menor):
                menor2=info_alumnos[2][i]
                notas_max_min[1][i]=menor2
                mn2=i#guardamos la posicion del alumno con la mas alta nota

        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]<menor3 and info_alumnos[2][i]>menor and info_alumnos[2][i]>menor2):
                menor3=info_alumnos[2][i]
                notas_max_min[1][i]=menor3
                mn3=i#guardamos la posicion del alumno con la mas alta nota

        print(menor3+" del alumno "+info_alumnos[0][mn3])
        print(menor2+" del alumno "+info_alumnos[0][mn2])
        print(menor+" del alumno "+info_alumnos[0][j]) 

    def ingresar_notas(self,info_alumnos):

        print("Ingrese las notas de la ")
        k=1
        for j in range(len(info_alumnos[0])):#lee la cantidad de alumnos
            for x in range(4):#primero ponemos las 4 pcs  
                notapcs_str=int(input("Nota de la "+str(k)+"pc del alumno "+info_alumnos[0][j].nombre+" : "))
                info_alumnos[1][j,x]=notapcs_str#ubicamos en la matriz [1]→notas,[j]→j-esimo alumno,[x]→x-esima nota (0-3/1pc-4pc)
                k=k+1
            parcial=input("Nota del parcial: ")
            info_alumnos[1][j][4]=parcial
            final=input("Nota del final: ")
            info_alumnos[1][j][5]=final
            k=0


class Alumno:
    def __init__(self,nombre,nseccion,curso):
        self.nombre=nombre
        self.nseccion=nseccion
        self.curso=curso

    def ver_notas(self,info_alumnos,nombre):
        print("Notas del alumno "+nombre+" : ")
        x=info_alumnos[0].index(nombre)#busca la posicion del alumno en la amtriz info_alumnos
        print("Notas PCS,parcial y final: "+info_alumnos[1][x])#imprime sus notas

class Notas:
    #info_alumnos[0][n]= Alumno(nalumno,nseccion,curso)
    #info_alumnos[1][n]= Alumno(nalumno,nseccion,curso)

    def __init__(self,alumno):
        self.alumno=alumno

    
    
    def promedio_alumnos(self,info_alumnos,nombre,notas_min_pc):
        notapcs=0
        #eliminando y guardando la pc más baja de cada alumno
        menor=20
        for x in range(len(info_alumnos[1])):
            for j in range(4):
                if info_alumnos[1][x][j]<menor:
                    menor=notas_min_pc[x]
            notas_min_pc[x] = menor  #guardando la nota mas baja de cada alumno
            menor=20 
        
        #poniendo las notas finales de cada alumno
        for x in range(len(info_alumnos[1])):  
            for j in range(4):
                if info_alumnos[1][x][j]==notas_min_pc[x]:#no lee la nota menor
                    continue
                notapcs=info_alumnos[1][x][j]+notapcs
            notapcs=notapcs/3
            info_alumnos[2][x]=(notapcs+info_alumnos[1][x][4]+info_alumnos[1][x][5])/3#alumnos[1][x][4]→parcial, alumnos[1][x][5]→final
            print("Promedio final del alumno "+nombre+" es: "+info_alumnos[2][x])
            notapcs=0
                
       
