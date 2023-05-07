import PySimpleGUI as sg
import os

current_dir = os.path.abspath(__file__)

relative_path = "icons\\config.png"
relative_path_2 = "icons\\help.png"
config_img = os.path.join('./', relative_path)
help_img = os.path.join('./', relative_path_2)

#front end

etiquetar_imagenes = [sg.Button('Etiquetar Imagenes', key= 'imagenes')]
generar_meme = [sg.Button('Generar Meme', key= 'meme')]
generar_collage= [sg.Button('Generar Collage', key='collage')]
salir = [sg.Button('Salir', key= 'salir')]

config = [sg.Button(key= 'config', image_filename=config_img, border_width=0, button_color="white", image_subsample=(3))]
ayuda = [sg.Button(key= 'help', image_filename=help_img, border_width=0, button_color="white")]



columna_vacia = [sg.Column([], background_color='white', size=(400,215))]
columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

column1_layout = []
column2_layout = [columna_vacia, etiquetar_imagenes, generar_meme, generar_collage, salir, columna_vacia2]
column3_layout = [config]
column4_layout = [ayuda]

column1 = sg.Column(column1_layout, size=(300, 600), background_color="white")
column2 = sg.Column(column2_layout, size=(250, 600), background_color="white")
column3 = sg.Column(column3_layout, size=(82, 600), background_color="white")
column4 = sg.Column(column4_layout, size=(82, 600), background_color="white")

layout = [[column1, column2, column3, column4]]


#interfaz
window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()