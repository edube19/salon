from uuid import NAMESPACE_URL
from seccion import *
#info_alumnos1=[[],[],[]]
#info_alumnos2=[[],[],[]]

seccion1=Seccion(1,'Matemática','Echendia')
seccion2=Seccion(2,'Fisica','Tafur')
print("Ingrese los alumnos: \n")
seccion1.agregar_alumno(seccion1.info_alumnos,'Matemática',1)
total_alumnos=seccion1.ver_lista(seccion1.info_alumnos,1)
print(total_alumnos)

seccion2.agregar_alumno(seccion2.info_alumnos,'Fisica',2)
total_alumnos=seccion2.ver_lista(seccion2.info_alumnos,2)
print(total_alumnos)

total_alumnos=seccion1.ver_lista(seccion1.info_alumnos,1)
print(total_alumnos)


seccion1.inicializar_notas(1,seccion1.info_alumnos)#1 para inicializar la columna de notas
seccion1.inicializar_notas(2,seccion1.info_alumnos)#2 para inicializar la columna de nota final
seccion1.inicializar_notas_min_pc(seccion1.notas_min_pc,seccion1.info_alumnos)#inicializa la nota mas baja de todas

seccion2.inicializar_notas(1,seccion2.info_alumnos)#1 para inicializar la columna de notas
seccion2.inicializar_notas(2,seccion2.info_alumnos)#2 para inicializar la columna de nota final
seccion2.inicializar_notas_min_pc(seccion2.notas_min_pc,seccion2.info_alumnos)#inicializa la nota mas baja de todas

c=1
print("Seccion 1")
while (c!=0):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    seccion1.recibir_notas(seccion1.info_alumnos,alumno)
    condicion=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
    c=condicion


seccion1.ver_notas_seccion(seccion1.info_alumnos,1)

seccion1.promedio_alumnos(seccion1.info_alumnos,seccion1.notas_min_pc)
seccion1.mayor_nota(seccion1.info_alumnos)
seccion1.menor_nota(seccion1.info_alumnos)

c=1
print("Seccion 2")
while (c!=0):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    seccion2.recibir_notas(seccion2.info_alumnos,alumno)
    condicion=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
    c=condicion


seccion2.ver_notas_seccion(seccion2.info_alumnos,2)

seccion2.promedio_alumnos(seccion2.info_alumnos,seccion2.notas_min_pc)
seccion2.mayor_nota(seccion2.info_alumnos)
seccion2.menor_nota(seccion2.info_alumnos)