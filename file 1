import matplotlib.pyplot as plt
import numpy as np

# --------- Vstupy od uživatele ----------
stred_input = input("Zadej souřadnice středu X Y (oddělené mezerou): ")
stred_x, stred_y = map(float, stred_input.split())

polomer = float(input("Zadej poloměr kružnice: "))
pocet_bodu = int(input("Zadej počet bodů na kružnici: "))
barva = input("Zadej barvu bodů (např. red, blue, green): ")
jednotka = input("Zadej jednotku (např. m, cm, mm): ")

# --------- Výpočet bodů ----------
uhly = np.linspace(0, 2*np.pi, pocet_bodu, endpoint=False)
x_body = stred_x + polomer * np.cos(uhly)
y_body = stred_y + polomer * np.sin(uhly)

# --------- Vykreslení ----------
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x_body, y_body, color=barva, label="Body na kružnici")
ax.scatter(stred_x, stred_y, color="black", marker="x", label="Střed")

# Kružnice pro vizualizaci
circle = plt.Circle((stred_x, stred_y), polomer, fill=False, linestyle="--", color="gray")
ax.add_artist(circle)

# Osy + jednotky
ax.set_xlabel(f"x [{jednotka}]")
ax.set_ylabel(f"y [{jednotka}]")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()

plt.show()
