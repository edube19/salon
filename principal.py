from uuid import NAMESPACE_URL
from seccion import *


seccion1=Seccion(1,'Matemática','Echendia')

print("Ingrese los alumnos: \n")
seccion1.agregar_alumno(info_alumnos,'Matemática',1)

total_alumnos=seccion1.ver_lista(info_alumnos,1)
print(total_alumnos)

seccion1.inicializar_notas(1)#1 para inicializar la columna de notas
seccion1.inicializar_notas(2)#2 para inicializar la columna de nota final
seccion1.inicializar_notas_min_pc(notas_min_pc)#inicializa la nota mas baja de todas

c=1

while (c!=0):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    seccion1.recibir_notas(info_alumnos,alumno)
    condicion=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
    c=condicion


seccion1.ver_notas_seccion(info_alumnos,1)

seccion1.promedio_alumnos(info_alumnos,notas_min_pc)
seccion1.mayor_nota(info_alumnos)
seccion1.menor_nota(info_alumnos)

seccion2=Seccion(2,'Matemática','Echendia')

#print(seccion2.ver_lista(info_alumnos,2))