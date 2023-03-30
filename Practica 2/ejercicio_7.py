#Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de
#palabras sin distinguir entre mayúsculas y minúsculas, en la frase.

texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

for caracter in texto:
    if caracter.isupper():
        print(f'Es mayuscula: {caracter}')
    elif caracter.islower():
        print(f'Es minuscula: {caracter}')
    else:
        print(f'No es una letra {caracter}')


palabras = texto.split()
print (palabras)
cant_p = len(palabras)
print(cant_p) #como hago para contar palabras sin tomar los numeros?