jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

caracter = input('Ingrese un caracter')[0]

palabras = jupyter_info.split()

for p in palabras:
    if caracter in p[0]:
        print(p)