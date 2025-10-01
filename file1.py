import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Kružnice s body")

# --------- Vstupy od uživatele ----------
stred_x = st.number_input("Zadej X souřadnici středu", value=0.0)
stred_y = st.number_input("Zadej Y souřadnici středu", value=0.0)
polomer = st.number_input("Zadej poloměr kružnice", value=1.0)
pocet_bodu = st.number_input("Zadej počet bodů na kružnici", min_value=1, value=10)
barva = st.color_picker("Vyber barvu bodů", value="#ff0000")  # barevný picker
jednotka = st.text_input("Zadej jednotku", value="m")

# --------- Výpočet bodů ----------
uhly = np.linspace(0, 2*np.pi, pocet_bodu, endpoint=False)
x_body = stred_x + polomer * np.cos(uhly)
y_body = stred_y + polomer * np.sin(uhly)

# --------- Vykreslení ----------
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x_body, y_body, color=barva, label="Body na kružnici")
ax.scatter(stred_x, stred_y, color="black", marker="x", label="Střed")

circle = plt.Circle((stred_x, stred_y), polomer, fill=False, linestyle="--", color="gray")
ax.add_artist(circle)

ax.set_xlabel(f"x [{jednotka}]")
ax.set_ylabel(f"y [{jednotka}]")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()

st.pyplot(fig)  # <--- místo plt.show()
