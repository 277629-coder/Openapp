import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io

st.title("Vykružnicuj ma")

# Rozbalovací okénko s informacemi
with st.expander("ℹ️ Více informací"):
    st.write("""
    Tento nástroj generuje body na kružnici.
    - Zadejte souřadnice středu X a Y
    - Zadejte poloměr a počet bodů
    - Vyberte barvu a jednotku
    Graf se automaticky vykreslí níže.
    - Jsem student VUT a za pomocí aplikace github a streamlit jsem vytvořil jednoduchou aplikaci
    """)

# --------- Vstupy od uživatele ----------
souřadnice = st.text_input("Zadej souřadnice středu X Y (oddělené mezerou)", "0 0")
try:
    stred_x, stred_y = map(float, souřadnice.split())
except:
    st.error("Zadej dvě čísla oddělená mezerou")
    st.stop()

polomer = st.number_input("Zadej poloměr kružnice", value=1.0)
pocet_bodu = st.number_input("Zadej počet bodů na kružnici", min_value=1, value=10)
barva = st.color_picker("Vyber barvu bodů", value="#ff0000")
jednotka = st.text_input("Zadej jednotku", value="m")
jmeno = st.text_input("Vaše jméno", "Jan Novak")
kontakt = st.text_input("Kontakt", "email@example.com")

# --------- Výpočet bodů ----------
uhly = np.linspace(0, 2*np.pi, pocet_bodu, endpoint=False)
x_body = stred_x + polomer * np.cos(uhly)
y_body = stred_y + polomer * np.sin(uhly)

# --------- Vykreslení grafu ----------
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x_body, y_body, color=barva, label="Body na kružnici")
ax.scatter(stred_x, stred_y, color="black", marker="x", label="Střed")
ax.set_xlabel(f"x [{jednotka}]")
ax.set_ylabel(f"y [{jednotka}]")
ax.set_aspect("equal")
ax.grid(True)
st.pyplot(fig)

# --------- Generování PDF přímo přes matplotlib ----------
if st.button("Generovat PDF"):
    pdf_bytes = io.BytesIO()

    # Vytvoříme novou figuru pro PDF, text nahoře, graf dole
    fig_pdf, (ax_text, ax_graph) = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios':[1,2]})
    
    # Textové informace
    ax_text.axis('off')
    text = f"""
Úloha: Kružnice s body
Jméno: {jmeno}
Kontakt: {kontakt}
Střed: ({stred_x}, {stred_y})
Poloměr: {polomer}
Počet bodů: {pocet_bodu}
Barva bodů: {barva}
Jednotka: {jednotka}
"""
    ax_text.text(0, 0.5, text, fontsize=12, verticalalignment='center', wrap=True)
    
    # Graf
    ax_graph.scatter(x_body, y_body, color=barva, label="Body")
    ax_graph.scatter(stred_x, stred_y, color="black", marker="x", label="Střed")
    ax_graph.set_xlabel(f"x [{jednotka}]")
    ax_graph.set_ylabel(f"y [{jednotka}]")
    ax_graph.set_aspect("equal")
    ax_graph.grid(True)
    
    fig_pdf.tight_layout()
    fig_pdf.savefig(pdf_bytes, format='pdf')
    plt.close(fig_pdf)
    pdf_bytes.seek(0)

    # Stáhnutí PDF
    st.download_button(
        label="Stáhnout PDF",
        data=pdf_bytes,
        file_name="kruzice.pdf",
        mime="application/pdf"
    )
