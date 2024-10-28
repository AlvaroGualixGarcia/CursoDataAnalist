import numpy as np
array = np.array([0,1,2,3,4,5])
array, type(array)
notas = [16,17,14,17,19,15]
ar_notas = np.array(notas, dtype=float)
ar_notas, type(ar_notas[0])
ar_notas_todas = np.array(([0,1,2,3,4,5], notas))
print(ar_notas_todas)