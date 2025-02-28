import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_productos.csv')
print(df)

datos = np.genfromtxt("ventas_productos.csv", delimiter=";", skip_header=1, usecols=(0, 1, 2))

print("Datos cargados:\n", datos)
print("Forma de los datos:", datos.shape)

df=pd.DataFrame(datos, columns=['Producto', 'Ventas', 'Precio'])
print(df)

df["Precio_Total"]= df["Ventas"]*df["Precio"]
print(df.head())
plt.bar(df["Producto"], df["Precio_Total"])
plt.title("Precio Total por Producto")
plt.xlabel("Producto")
plt.ylabel("Precio Total")
plt.show()
plt.savefig("Precio_Total_por_Producto.png")
