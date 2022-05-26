from uuid import NAMESPACE_URL
from seccion import *


seccion1=Seccion(1,'Matemática','Echendia')

print("Ingrese los alumnos: \n")
seccion1.agregar_alumno(info_alumnos,'Matemática',1)

total_alumnos=seccion1.ver_lista(info_alumnos,1)
print(total_alumnos)
c=1
n=0
seccion1.inicializar_notas(1)#1 para inicializar la columna de notas
seccion1.inicializar_notas(2)#2 para inicializar la columna de nota final
seccion1.inicializar_notas_min_pc(notas_min_pc)#inicializa la nota mas baja de todas

#for i in range(total_alumnos):



while (c!=0 and n!=total_alumnos):#Ingresar notas de los alumnos
    nalumno=input("Ingresar notas del alumno ")
    pc1=int(input("PC 1: "))
    pc2=int(input("PC 2: "))
    pc3=int(input("PC 3: "))
    pc4=int(input("PC 4: "))
    parcial=int(input("Parcial: "))
    final=int(input("Final: "))
    seccion1.ingresar_notas(nalumno,pc1,pc2,pc3,pc4,parcial,final)
    seccion1.ver_notas(info_alumnos,nalumno)
    n=n+1
    condicion=int(input("Notas ingresadas. ¿Ingresar otro? (1→SI / 0→NO) "))
    if (n==total_alumnos):
        c=0
    else:
        c=condicion
#nalumno=input("Ver notas del alumno: ")
#seccion1.ver_notas(info_alumnos,nalumno)

#seccion1.ver_notas_seccion(info_alumnos,1)

seccion1.promedio_alumnos(info_alumnos,notas_min_pc)
