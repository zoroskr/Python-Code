import PySimpleGUI as sg
import json
import os

current_dir = os.path.abspath(__file__)

relative_path = "icons\\icon_add.png"
relative_path_2 = "icons\\ver_mas.png"

icon_add = os.path.join('./', relative_path)
ver_mas = os.path.join('./', relative_path_2)



with open('perfiles.json', 'r', encoding='utf-8') as archivo: 
    datos = json.load(archivo) #nos guardamos los perfiles del json

agregar_perfil = sg.Button(enable_events=True, key='add', button_color='white', border_width=0, image_subsample=(4), image_filename=icon_add) #boton para añadir perfiles
otros_perfiles = [sg.Button(enable_events=True, key='otros', button_color='white', border_width=0, size=(20,5), pad=(135,10), image_subsample=(3), image_filename=ver_mas)]

perfiles = [agregar_perfil]

for perfil in datos['perfiles'][0:2]:
    perfil_boton = sg.Button(enable_events=True, key=perfil['nombre'], button_color='white', border_width=0, image_filename=perfil['imagen'])
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

#primera ventana

ok = False
menu = False

window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'otros':
        ok = True
        break
    else:
        menu = True
        break
window.close()

if (menu == True):
    import menu_principal

#segunda ventana
if (ok == True):

    perfiles.clear()
    for perfil in datos['perfiles'][2:]:
        perfil_boton = sg.Button(enable_events=True, key=perfil['nombre'], button_color='white', border_width=0, image_filename=perfil['imagen'])
        perfiles.append(perfil_boton)

    titulo2 = [sg.Text('UNLP Image', auto_size_text=True, text_color='black', background_color='white', font=('GabrielWeiss'))]

    columna_vacia3 = [sg.Column([], background_color='white', size=(400,215))]
    columna_vacia4 = [sg.Column([], background_color='white', size=(400,400))]

    column4_layout = [columna_vacia3, perfiles, columna_vacia4]
    column3_layout = [titulo2]

    column3 = sg.Column(column3_layout, size=(175,600), background_color="white")
    column4 = sg.Column(column4_layout, size=(415, 600), background_color="white", key='-column2-')

    layout2 = [[column3, column4]]


    window2 = sg.Window("UNLP Image", layout2, background_color='white', size=(800,600))
    while True:
        event, values = window2.read()
        if event == sg.WIN_CLOSED:
            break
        

    window2.close()

