# =========================================================
# Practicando las graficas en formato de Barras Combinadas.

import matplotlib.pyplot as plt

asteroides_pequenos = (2, 4, 3, 1, 8)
asteroides_grandes = (15, 18, 20, 0, 0)

separacion = [0, 1, 2, 3, 4]
grueso = 0.5

plt.title("Comparativa entre tamaños de asteroides")
plt.xticks(separacion,("Detección 1", "Detección 2", "Detección 3",
                       "Detección 4", "Detección 5"))
bar_1 = plt.bar(separacion, asteroides_pequenos, grueso)
bar_2 = plt.bar(separacion, asteroides_grandes, grueso,
                bottom = asteroides_pequenos)

plt.ylabel("Tamaños registrados")
plt.yticks([0, 4, 8, 12, 16, 20, 24, 28, 32])
plt.legend((bar_1[0],bar_2[0]),
           ("Asteroides grandes", "Asteroides pequeños"))
plt.show()

# =========================================================
