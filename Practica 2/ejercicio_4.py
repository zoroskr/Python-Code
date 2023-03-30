evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

#dividimos el texto en palabras
texto = evaluar.split("\n")
titulo_separado= texto[0].split()
if len(titulo_separado) <= 11:
    print('ok')
else:
    print('not ok')
evaluar = evaluar.replace(evaluar[0:len(texto[0])],"")
resumen= evaluar.split(".")
for i in range(0, len(resumen)):
    lista_act=resumen[i].split()
    cantResumen=len(lista_act)
    if (cantResumen <= 12):
        print('facil de leer')
    else:
        if (cantResumen >= 13) and (cantResumen <=17):
            print('aceptalbe')
        else:
            if (cantResumen >= 18) and (cantResumen <=25):
                print('dificil de leer')
            else:
                if (cantResumen > 25):
                    print('muy dificil')


