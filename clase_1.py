# =========================================================

import matplotlib.pyplot as plt

carne = [10, 99, 20]
tiempo_1 = ["Junio", "Julio", "Agosto"]

pollo = [15, 60, 38]
tiempo_2 = ["Junio", "Julio", "Agosto"]

plt.plot(tiempo_1, carne, marker ="o",
         linestyle= "--", color="r", label="Carne")

plt.plot(tiempo_2, pollo, marker ="d",
         linestyle= "--", color="b", label="Pollo")

plt.xlabel("Meses del año")
plt.ylabel("Carne consumida (kg)")
plt.title("Consumo de carne al mes")
plt.legend()
plt.show()

# =========================================================