import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi

sns.set(style="whitegrid", context="notebook")

class GotaEnAceite:
    def __init__(self, r0, h0, dr_dt, dh_dt, tiempo_max=10, pasos=100):
        self.r0 = r0
        self.h0 = h0
        self.dr_dt = dr_dt
        self.dh_dt = dh_dt
        self.t = np.linspace(0, tiempo_max, pasos)

        # Cálculos físicos
        self.r = self.r0 + self.dr_dt * self.t
        self.h = self.h0 + self.dh_dt * self.t
        self.d = 2 * self.r
        self.V = pi * (self.r ** 2) * self.h

        # Derivada del volumen
        self.dv_dt = pi * (2 * self.r * self.h * self.dr_dt + self.r ** 2 * self.dh_dt)

        # DataFrame con resultados
        self.df = pd.DataFrame({
            "Tiempo (s)": self.t,
            "Radio (mm)": self.r,
            "Altura (mm)": self.h,
            "Diametro (mm)": self.d,
            "Volumen (mm³)": self.V,
            "dV/dt (mm³/s)": self.dv_dt
        })

    def mostrar_resultados(self):
        print("\n-- Datos iniciales y finales --")
        print(f"Radio inicial: {self.r0} mm")
        print(f"Altura inicial: {self.h0} mm")
        print(f"Tasa de cambio de radio: {self.dr_dt} mm/s")
        print(f"Tasa de cambio de altura: {self.dh_dt} mm/s")
        print(self.df.iloc[[0, -1]])

    def graficar(self):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        sns.lineplot(data=self.df, x="Tiempo (s)", y="Diametro (mm)", ax=axes[0], color="blue")
        axes[0].set_title("Diámetro vs Tiempo")

        sns.lineplot(data=self.df, x="Tiempo (s)", y="Volumen (mm³)", ax=axes[1], color="orange")
        axes[1].set_title("Volumen vs Tiempo")

        sns.lineplot(data=self.df, x="Tiempo (s)", y="dV/dt (mm³/s)", ax=axes[2], color="green")
        axes[2].set_title("dV/dt vs Tiempo")

        fig.suptitle("Crecimiento de una gota en aceite con altura variable", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def exportar_datos(self, nombre_archivo):
        self.df.to_csv(nombre_archivo, index=False)
        print(f"Datos exportados a '{nombre_archivo}'")

# -------------------------
# Datos de la simulación
# -------------------------

r0 = 1.0      # Radio inicial en mm
h0 = 1.0      # Altura inicial en mm
dr_dt = 0.1   # Tasa de cambio de radio en mm/s
dh_dt = 0.1   # Tasa de cambio de altura en mm/s
tiempo = 10   # Tiempo total de simulación en segundos

# Crear y ejecutar la simulación
gota = GotaEnAceite(r0, h0, dr_dt, dh_dt, tiempo_max=tiempo)
gota.mostrar_resultados()
gota.graficar()

# Exportar CSV si se desea
exportar = True
if exportar:
    nombre = "gota_datos.csv"
    gota.exportar_datos(nombre)
