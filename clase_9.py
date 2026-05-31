# =========================================================
# Practicando las graficas en formato de Barras Combinadas.

import matplotlib.pyplot as plt

plt.figure(figsize=[8,7])

# Cantidad de materia esperadas en distintas galaxias:
materia = [1000, 1800, 1200, 950]
galaxias = ["Galaxia 1", "Galaxia 2", "Galaxia 3", "Galaxia 4"]

plt.plot(galaxias, materia, marker = "d",
         linestyle = "--", color = "r", label = "Materia esperada")

plt.legend()
plt.xlabel("Galaxias estudiadas")
plt.title("Materia estimada vs materia hallada en distintas galaxias")

# Materia en galaxias:
galaxias = ["Galaxia 1", "Galaxia 2", "Galaxia 3", "Galaxia 4"]
materia_2 = [3000, 3800, 3200, 2050]
plt.bar(galaxias, materia_2)

plt.show()

# =========================================================
