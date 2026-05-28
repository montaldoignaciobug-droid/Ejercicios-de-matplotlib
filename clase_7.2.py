# =========================================================
# Practicando las graficas en formato de Boxplot.

import matplotlib.pyplot as plt

plt.figure(figsize=[7,6])

tamaños = [20, 23, 19, 27, 26, 17, 21]
plt.boxplot(tamaños)
plt.ylabel("Tamaños en metros")
plt.title("Tamaño de asteroides medianos")
plt.show()

# El mismo codigo de "clase_7.py" pero sin las anomalias.
# =========================================================