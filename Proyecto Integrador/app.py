import inicio_ventana
import menu_principal_ventana
import PySimpleGUI


ventana_principal = inicio_ventana.VentanaPrincipal()
ventana_principal.iniciar_ventana()

'''
ventana_principal2 = inicio_ventana.VentanaPrincipal(2)
ventana_principal2.iniciar_ventana()

menu_ventana = menu_principal_ventana.VentanaMenu()
menu_ventana.iniciar_ventana()'''


'''window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Abrir ventana 1":
        open_window1()
    elif event == "Abrir ventana 2":
        open_window2()'''