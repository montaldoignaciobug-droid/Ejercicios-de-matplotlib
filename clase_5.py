# =========================================================
# Practicando las graficas en formato de Pie.

import matplotlib.pyplot as plt

plt.figure(figsize=[6,5])
elementos = ["Dióxido de carbono", "Nitrógeno", "Argón", "Otros"]
porcentajes = [95.3, 2.7, 1.6, 0.4]
destacar = [0, 0, 0, 0.1]

plt.style.use("ggplot")
plt.title("Elementos en la atmosfera de Marte")
plt.pie(x = porcentajes, explode = destacar,
        labels = elementos, autopct="%.2f%%", shadow = True, startangle=20)
plt.axis("equal")
plt.legend(loc="upper left")

plt.show()

# =========================================================