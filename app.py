import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Body na kružnici")

# Vstupy od uživatele
center_x = st.number_input("Souřadnice středu X:", value=0.0, step=0.1)
center_y = st.number_input("Souřadnice středu Y:", value=0.0, step=0.1)
radius = st.number_input("Poloměr kružnice:", value=1.0, min_value=0.1, step=0.1)
n_points = st.number_input("Počet bodů:", value=20, min_value=3, max_value=500, step=1)
color = st.color_picker("Barva bodů:", "#ff0000")

# Výpočet bodů
theta = np.linspace(0, 2*np.pi, int(n_points)+1)  # +1 pro uzavření kružnice
x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

# Vykreslení grafu
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x, y, c=color)
ax.plot(x, y, c=color, alpha=0.5)  # spojnice bodů

# Zachování kruhového poměru
ax.set_aspect("equal", adjustable="box")

# Popisky os s jednotkami
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")

# Síť + osy
ax.grid(True)
ax.set_title("Kružnice")

st.pyplot(fig)

