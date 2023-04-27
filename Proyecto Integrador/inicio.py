import PySimpleGUI as sg
import json
with open('C:/Users/elmun/Desktop/Zoros/Primer Semestre - 2do año/Python/Python Code/Python-Code/Proyecto Integrador/perfiles.json', 'r', encoding='utf-8') as archivo: 
    datos = json.load(archivo) #nos guardamos los perfiles del json

agregar_perfil = sg.Button(enable_events=True, key='add', button_color='white', border_width=0, image_subsample=(4), image_filename='C:/Users/elmun/Desktop/Zoros/Primer Semestre - 2do año/Python/Python Code/Python-Code/Proyecto Integrador/icon_add.png') #boton para añadir perfiles
otros_perfiles = [sg.Button(enable_events=True, key='otros', button_color='white', border_width=0, size=(20,5), pad=(135,10), image_subsample=(3), image_filename='C:/Users/elmun/Desktop/Zoros/Primer Semestre - 2do año/Python/Python Code/Python-Code/Proyecto Integrador/ver_mas.png')]

perfiles = [agregar_perfil]

for perfil in datos['perfiles'][0:1]:
    perfil_boton = sg.Button(enable_events=True, key=perfil['nombre'], button_color='white', border_width=0, image_subsample=(4), image_filename=perfil['imagen'])
    perfiles.append(perfil_boton)

#front end

titulo = [sg.Text('UNLP Image', auto_size_text=True, text_color='black', background_color='white', font=('GabrielWeiss'))]

columna_vacia = [sg.Column([], background_color='white', size=(400,215))]
columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

column2_layout = [columna_vacia, perfiles, otros_perfiles, columna_vacia2]
column1_layout = [titulo]

column1 = sg.Column(column1_layout, size=(175,600), background_color="white")
column2 = sg.Column(column2_layout, size=(415, 600), background_color="white", key='-column2-')

layout = [[column1, column2]]


#interfaz
window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'add':
        print(perfiles)

window.close()
