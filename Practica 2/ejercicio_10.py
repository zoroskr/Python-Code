from statistics import mean
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def prom (notas):
    return sum(notas) / 2

nombres = nombres.split(',') # separamos los nombres 

dicci= dict(zip(nombres, zip(notas_1, notas_2))) # creamos un diccionario teniendo como clave los nombres y valor una tupla con las 2 notas

prom_estudiantes = list(map(prom, dicci.values())) #creamos una lista con los promedios de cada estudiante

promedio_total = mean(prom_estudiantes) #sacamos el promedio del curso con mean

#D
estudiante_max = max(zip(nombres, prom_estudiantes), key= lambda x: x[1])[0] #sacamos el maximo, indicandole que busque en el elemento de la tupla en la pos 1 (el promedio), luego nos guardamos el nombre del estudiante

estudiante_min = min(zip(nombres, prom_estudiantes), key= lambda x: x[1])[0]

print (prom_estudiantes)
print (promedio_total)
print (estudiante_max)
print(estudiante_min)