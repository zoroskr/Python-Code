frase = input('Ingrese una frase: ')

frase = frase.lower()
heterograma= True
for c in frase:
    if c.isalpha():
        if frase.count(c) > 1:
            heterograma= False

print(heterograma)