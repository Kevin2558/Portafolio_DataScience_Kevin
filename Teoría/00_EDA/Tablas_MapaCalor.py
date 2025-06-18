import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\kevin\OneDrive\Escritorio\Titanic-Dataset.csv") # Subir el dataset.

df = pd.DataFrame(data) # Transformar el dataset en un dataframe.

# Aqui hacemos una tabla que muestra la suma de sobrevivientes por sexo
df.groupby("Sex")["Survived"].sum() 

# Aquí separamos un poco mas la tabla obteniendo la suma de sobrevivientes por sexo
# y además los separamos por clase
df.groupby(["Pclass","Sex"]).agg({"Survived":"sum"})

# Aquí muestra el total de  personas
df.groupby(["Pclass","Sex"]).agg({"Survived":"count"})

# Aqui se muestra las dos tablas anteriores
df.pivot_table(columns=["Sex","Pclass"], values="Survived", aggfunc=["sum","count"])

# Aquí cruza las columnas a modo de promedio (creo) y normalize="index" normaliza los valores
pd.crosstab(df["Sex"],df["Survived"],normalize="index")

# Obtenemos las correlaciones entre las distintas variables del dataset
df.corr(numeric_only=True) # Mientras mas se acercan a 1 o -1 son mas correlacionadas

import seaborn as sns

# Nos entrega las correlaciones en un mapa de calor mas estetico
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()

g = sns.FacetGrid(df,col="Sex",row="Pclass",aspect=2)
g.map(plt.hist,"Age",bins=10)
plt.show()
