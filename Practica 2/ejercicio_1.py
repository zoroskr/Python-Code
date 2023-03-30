from collections import Counter
readme_numpy = '''NumPy is the fundamental package for scientific computing with Python.
Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

lol lol lol lol

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities'''

lineas = readme_numpy.splitlines() #separamos el texto en lineas

#for l in lineas:
#    if 'https' in l or 'http' in l:
#        print(l)

texto = readme_numpy.lower() 
palabras = texto.split()
cuenta = Counter(palabras)
maximo = cuenta.most_common(1)[0][0]
print(maximo)




