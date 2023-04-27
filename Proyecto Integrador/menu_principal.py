import PySimpleGUI as sg


#front end
perfil_boton = [sg.Button(enable_events=True, key='nombre', button_color='white', border_width=0, image_subsample=(4), image_filename='C:/Users/elmun/Desktop/Zoros/Primer Semestre - 2do año/Python/Python Code/Python-Code/Proyecto Integrador/icon_add.png')]
perfil_nombre = [sg.Text('-Nombre-', auto_size_text=True, text_color='black', background_color='white', font=('GabrielWeiss'), pad=(35,10))]

etiquetar_imagenes = [sg.Button('Etiquetar Imagenes')]
generar_meme = [sg.Button('Generar Meme')]
generar_collage= [sg.Button('Generar Collage')]
salir = [sg.Button('Salir')]




columna_vacia = [sg.Column([], background_color='white', size=(400,400))]
columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

column2_layout = [columna_vacia, etiquetar_imagenes, generar_meme, generar_collage, salir, columna_vacia2]
column1_layout = [perfil_boton, perfil_nombre]

column1 = sg.Column(column1_layout, size=(200,800), background_color="red")
column2 = sg.Column(column2_layout, size=(400, 800), background_color="blue", scrollable=True)

layout = [[column1, column2]]


#interfaz
window = sg.Window("UNLP Image", layout, background_color='white')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()