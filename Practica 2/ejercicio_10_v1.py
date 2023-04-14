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


list= nombres.split(",")
dicci=dict()

for a in range(0,len(list)):
    dicci[list[a]] = notas_1[a],notas_2[a]
print(dicci)
promtotal=0
min = 99999
list_prom = []
alumno_min = ''
prom_max= -1
for a in range(0,len(list)):
    tupla_notas=dicci.get(list[a])
    prom=(tupla_notas[0] + tupla_notas[1]) / 2
    if min > tupla_notas[0] or min > tupla_notas[1]:
        min = tupla_notas[0]
        alumno_min = list[a]
    if prom > prom_max:
        prom_max = prom
        alumno_max=list[a]
    list_prom.append(prom)
    promtotal+= prom
promtotal=promtotal/len(list)


prom_max=max(list_prom)
print(promtotal)
print(alumno_max)
print(alumno_min)