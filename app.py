import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

st.title("Body na kružnici")

# ---- Vstupy od uživatele ----
center_x = st.number_input("Souřadnice středu X:", value=0.0, step=0.1)
center_y = st.number_input("Souřadnice středu Y:", value=0.0, step=0.1)
radius = st.number_input("Poloměr kružnice [m]:", value=1.0, min_value=0.1, step=0.1)
n_points = st.number_input("Počet bodů:", value=20, min_value=3, max_value=500, step=1)
color = st.color_picker("Barva bodů:", "#ff0000")

# ---- Výpočet bodů ----
theta = np.linspace(0, 2*np.pi, int(n_points)+1)  # +1 pro uzavření kružnice
x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

# ---- Graf ----
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x, y, c=color, label="Body")
ax.plot(x, y, c=color, alpha=0.5, label="Spojnice")
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.grid(True)
ax.set_title("Kružnice")
ax.legend()

st.pyplot(fig)

# ---- Funkce pro generování PDF ----
def generate_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Nadpis
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Výsledná úloha - Body na kružnici")

    # Parametry úlohy
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Střed: ({center_x}, {center_y})")
    c.drawString(50, height - 120, f"Poloměr: {radius} m")
    c.drawString(50, height - 140, f"Počet bodů: {n_points}")
    c.drawString(50, height - 160, f"Barva bodů: {color}")

    # Autor + kontakt
    c.drawString(50, height - 200, "Autor: Jan Novák")
    c.drawString(50, height - 220, "Kontakt: jan.novak@email.cz")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ---- Tlačítko pro stažení PDF ----
pdf_buffer = generate_pdf()
st.download_button(
    label="📄 Stáhnout report v PDF",
    data=pdf_buffer,
    file_name="kruznice_report.pdf",
    mime="application/pdf"
)

# ---- Sidebar ----
st.sidebar.title("O projektu")
st.sidebar.markdown(
    """
    **Autor:** Jan Novák  
    **Použité technologie:**  
    - Streamlit  
    - NumPy  
    - Matplotlib  
    - ReportLab (export do PDF)  

    Tento projekt ukazuje generování a vykreslení bodů na kružnici
    s možností interaktivního nastavení parametrů.
    """
)
