# =========================================================
# Practicando las graficas en formato lineal

import matplotlib.pyplot as plt

Irradiancia_solar = [940, 902, 870, 1.54, 807, 910]
tiempo_1 = ["18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]

plt.plot(tiempo_1, Irradiancia_solar, marker ="o",
         linestyle= "--", color="darkorange", label="Luz solar")

plt.xlabel("Horas del día")
plt.ylabel("Irradiancia solar en W/m²")
plt.title("Irradiación del sol en un día con eclipse")
plt.legend()
plt.show()

# =========================================================
