import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("Tabla de datos:")
print(df)

# Graficar las ventas
plt.figure(figsize=(8, 5))
plt.plot(df["Mes"], df["Ventas"], marker="o", linestyle="-", color="b", label="Ventas")

# Configurar etiquetas y título
plt.xlabel("Mes")
plt.ylabel("Monto ($)")
plt.title("Ventas por Mes")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()