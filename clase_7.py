# =========================================================
# Practicando las graficas en formato de Boxplot.

import matplotlib.pyplot as plt

plt.figure(figsize=[7,6])

tamaños = [20, 23, 19, 27, 26, 17, 21, 80, 76]
plt.boxplot(tamaños)
plt.ylabel("Tamaños en metros")
plt.title("Tamaño de asteroides medianos")
plt.show()

# El codigo muestra dos anomalias (los objetos "80" y "76").
# =========================================================