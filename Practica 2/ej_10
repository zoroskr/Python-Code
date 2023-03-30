nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'D
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica',
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge'
'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo',
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
39, 15, 74, 33, 57, 10]

notas1 = set(notas_1)
notas2 = set(notas_2)
notas_3 = notas1.union(notas2)
print(notas_3)
list= nombres.split()
dicci=dict()
promtotal=0
print(notas_2)
print(len(notas_2))
print(len(notas_1))
print(len(list))
for a in range(0,len(list)):
    prom=(notas_1[a] + notas_2[a])
    dicci[list[a]]= prom
    promtotal+= prom
promtotal=promtotal/len(list)
prom_max=max(dicci.values())
for al in dicci:
    if dicci[al]== prom_max:
        al_max=al
print(al_max)
