frase = '''Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo
tres tristes tigres'''

palabra = input()
palabra = palabra.lower()

frase = frase.lower()
lista = frase.split()

num_palabra= lista.count(palabra)
print(lista)
print(num_palabra)