import csv
from collections import Counter

def usuarios_mas_frecuentes(orden = None):
    with open('log_catedras.csv', 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        usuarios = [fila['Nombre completo del usuario'] for fila in lector_csv]
        conteo_usuarios = Counter(usuarios).most_common(5)
        if orden == 'A':
            conteo_usuarios = conteo_usuarios[::-1]
        return conteo_usuarios
        
mas_frecuentes = usuarios_mas_frecuentes()
print('-'*50)
print('Usuario en el sistema  Cantidad de accesos')
print('-'*50)

for i in range(5):
    columna = mas_frecuentes[i][0].ljust(23) + str(mas_frecuentes[i][1]).ljust(20)
    print(columna)