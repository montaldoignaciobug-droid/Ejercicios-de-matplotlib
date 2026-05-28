# =========================================================
# Practicando las graficas en formato de Donut.

import matplotlib.pyplot as plt

plt.figure(figsize=[7,6])
elementos = ["Hidrógeno", "Helio", "Metales"]
porcentajes = [70, 28, 2]
destacar = [0, 0, 0.1]

plt.style.use("ggplot")
plt.title("Elementos en la atmosfera estelar de las estrellas")
plt.pie(x = porcentajes, explode = destacar,
        labels = elementos, autopct="%.2f%%", shadow = True, startangle=150)
plt.axis("equal")
plt.legend(loc="upper left")

circle = plt.Circle(xy=(0,0), radius = 0.65, facecolor = "white")
plt.gca().add_artist(circle)
plt.show()

# =========================================================
