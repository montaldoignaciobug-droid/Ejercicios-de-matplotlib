# =========================================================
# Practicando las graficas en formato de barras.

import matplotlib.pyplot as plt

plt.figure(figsize=[10,6])
legumbres = ["Silice", "Magnesio ", "Óxido de hierro", "Óxido de calcio", "Otros"]
consumo = [43, 32, 9, 8.5, 7.5]

plt.bar(legumbres, consumo)
plt.xlabel("Material presente")
plt.ylabel("Porcentaje del mineral")
plt.title("Propiedades de la peridotita")
plt.show()

# =========================================================