import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import io

st.title("Kružnice s body")

# Rozbalovací okénko s informacemi
with st.expander("ℹ️ Více informací"):
    st.write("""
    Tento nástroj generuje body na kružnici.
    - Zadejte souřadnice středu X a Y
    - Zadejte poloměr a počet bodů
    - Vyberte barvu a jednotku
    Graf se automaticky vykreslí níže.
    - Jsem student VUT v Brně a za pomocí aplikace github a streamlit jsem vytvořil tuto jednoduchou aplikaci
    """)

# --------- Vstupy od uživatele ----------
souřadnice = st.text_input("Zadej souřadnice středu X Y (oddělené mezerou)", "0 0")
try:
    stred_x, stred_y = map(float, souřadnice.split())
except:
    st.error("Zadej dvě čísla oddělená mezerou")
    st.stop()  # zastaví vykreslení, dokud nejsou validní hodnoty

polomer = st.number_input("Zadej poloměr kružnice", value=1.0)
pocet_bodu = st.number_input("Zadej počet bodů na kružnici", min_value=1, value=10)
barva = st.color_picker("Vyber barvu bodů", value="#ff0000")  # barevný picker
jednotka = st.text_input("Zadej jednotku", value="m")
jmeno = st.text_input("Vaše jméno", "Jan Novak")
kontakt = st.text_input("Kontakt", "email@example.com")

# --------- Výpočet bodů ----------
uhly = np.linspace(0, 2*np.pi, pocet_bodu, endpoint=False)
x_body = stred_x + polomer * np.cos(uhly)
y_body = stred_y + polomer * np.sin(uhly)

# --------- Vykreslení ----------
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x_body, y_body, color=barva, label="Body na kružnici")
ax.scatter(stred_x, stred_y, color="black", marker="x", label="Střed")

ax.set_xlabel(f"x [{jednotka}]")
ax.set_ylabel(f"y [{jednotka}]")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)

st.pyplot(fig)

import tempfile

# --------- Generování PDF ----------
if st.button("Generovat PDF"):
    # Uložíme graf do dočasného souboru
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        fig.savefig(tmpfile.name, format="png")
        graf_path = tmpfile.name

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Úloha: Kružnice s body", ln=True)
    pdf.cell(0, 10, f"Jméno: {jmeno}", ln=True)
    pdf.cell(0, 10, f"Kontakt: {kontakt}", ln=True)
    pdf.cell(0, 10, f"Střed: ({stred_x}, {stred_y})", ln=True)
    pdf.cell(0, 10, f"Poloměr: {polomer}", ln=True)
    pdf.cell(0, 10, f"Počet bodů: {pocet_bodu}", ln=True)
    pdf.cell(0, 10, f"Barva bodů: {barva}", ln=True)
    pdf.cell(0, 10, f"Jednotka: {jednotka}", ln=True)
    pdf.ln(10)

    # Přidáme graf jako obrázek z dočasného souboru
    pdf.image(graf_path, x=10, y=None, w=180)

    # Uložíme PDF do BytesIO pro Streamlit
    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)

    st.download_button(
        label="Stáhnout PDF",
        data=pdf_bytes,
        file_name="kruzice.pdf",
        mime="application/pdf"
    )
