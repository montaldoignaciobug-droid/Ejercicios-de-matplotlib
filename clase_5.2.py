# =========================================================
# Practicando las graficas en formato de Pie.

import matplotlib.pyplot as plt

plt.figure(figsize=[6,5])
elementos = ["Nitrógeno", "Oxígeno", "Otros"]
porcentajes = [78.08, 20.95, 0.97]
destacar = [0, 0, 0.1]

plt.style.use("ggplot")
plt.title("Elementos en la atmosfera de la Tierra")
plt.pie(x = porcentajes, explode = destacar,
        labels = elementos, autopct="%.2f%%", shadow = True, startangle=20)
plt.axis("equal")
plt.legend(loc="upper left")

plt.show()

# =========================================================