import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\kevin\OneDrive\Escritorio\Titanic-Dataset.csv") # Subir el dataset.

df = pd.DataFrame(data) # Transformar el dataset en un dataframe.

datos_1 = np.array([1,2,3,4,5,12,11,15])
datos_2 = np.array([1,2,3,4,5,12,11,15,200])

mean_1 = np.mean(datos_1)
mean_2 = np.mean(datos_2)

print(mean_1)
print(mean_2) # La media se ve afectada por datos outliers (200)

median_1=np.median(datos_1)
median_2=np.median(datos_2)
print(median_1)
print(median_2) # En este caso, los outliers no afectan en demasía

df["Age"].describe() # Índices estadísticos pero solo para una columna

df["Age"].isnull().mean() # Cerca del 20% de los datos es nulo, esto nos sirve
                          # para saber que decisión tomar, entre quitarlos,
                          # imputarlos (cambiarlos).

# Usamos la media para representar los nulos si la distribución es bien estándar

df["Age"].hist() # Notemos que no es simétrico por lo que es mejor usar la
                 # mediana.
plt.show() # En vscode para que se muestren los graficos usamos este codigo

# df.fillna() rellena los valores nulos por la mediana en este caso
df["Age_imputed"] = df["Age"].fillna(df["Age"].median()) 

# Calculo de los cuartiles para la columna edad ya rellenada
Q1 = df["Age_imputed"].quantile(0.25)
Q3 = df["Age_imputed"].quantile(0.75)
IQR = Q3 - Q1

cota_inferior = Q1 - 1.5 * IQR # Rango en donde los datos que estan fuera podrian
                               # ser considerados outliers
cota_superior = Q3 + 1.5 * IQR

plt.hist(df["Age_imputed"]) # Histograma de la edad rellanada
# Aquí embellecemos el grafico dandole los nombres segun corresponda
plt.title("Age imputed") 
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show() # En este caso, los datos nulos se reemplazaron por la mediana y así
           # se ve mas centrado.

# Aqui visualizaremos los datos de la edad rellanda vista como un conjunto
# así poder observar los datos outliers
plt.boxplot(df["Age_imputed"])
plt.title("Age imputed")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Comparación de los graficos para sobrevivientes y no sobrevivientes

# Aqui generamos una matriz que guarda el valor de la edad de las filas que sobrevivieron
survived = df[df["Survived"] == 1]["Age"].dropna() # dropna es eliminación de
                                                   # valores nulos

# Aqui por el contrario se genera una matriz que guardar el valor de la edad de las filas
# que no sobrevivieron
not_survived = df[df["Survived"] == 0]["Age"].dropna()

plt.hist(survived,bins=15, alpha=0.7, label="Survived") # bins cantidad de
                                                        # puntos a usar
plt.hist(not_survived,bins=15, alpha=0.7, label="Not Survived")
plt.title("Comparación de edades (Supervivencia)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# De este histograma podemos observar que en edades inferiores hay una tendencia
# a la supervivencia. En el rango de edad 20-30 no hay una clara tendencia
# a la supervivencia o a la no. Y en rangos mayores tiende a ser equilibrado.

# Aquí guardamos las filas de las personas que cumplan con la edad
df_jovenes = df[(df["Age"] >18) & (df["Age"] < 40)]

# Volvemos a hacer lo de antes pero con un grupo seleccionado de edades
survived_jovenes = df_jovenes[df_jovenes["Survived"] == 1]["Age"].dropna() # dropna es eliminación de
                                                                           # valores nulos
not_survived_jovenes = df_jovenes[df_jovenes["Survived"] == 0]["Age"].dropna()

plt.hist(survived_jovenes,bins=5, alpha=0.7, label="Survived") # bins es la cantidad de elementos a tomar por barra
                                                               # del histogram y alpha la transparencia del grafico 
plt.hist(not_survived_jovenes,bins=5, alpha=0.7, label="Not Survived")
plt.title("Comparación de edades [18-40] (Supervivencia)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Da igual las edades que tenian para definir si sobrevivian o no, menos en los
# rangos de preponderacia, que serían los extremos del histograma.

# Ahora repetimos el proceso para las columnas Pclass, Sex, FamilySize

df["Pclass"].hist(bins=3,rwidth=0.7) # rwidth controla la anchura de las barras

df["Pclass"].isnull().mean()

# Notemos que no hay datos nulos por lo que no necesitamos imputar, son bien estables.

plt.boxplot(df["Pclass"]) 
plt.title("Pclass")
plt.xlabel("Pclass")
plt.ylabel("Frequency")
plt.show()

# Ahora vamos a comparar la frecuencia de sobrevivencia dependiendo de la clase

survived = df[df["Survived"] == 1]["Pclass"].dropna() # dropna es eliminación de valores nulos
not_survived = df[df["Survived"] == 0]["Pclass"].dropna()

plt.hist(survived,bins=3, alpha=0.7, label="Survived",rwidth=0.7) # bins cantidad de puntos a usar
plt.hist(not_survived,bins=3, alpha=0.7, label="Not Survived",rwidth=0.7)
plt.title("Comparación de clases (Supervivencia)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# La mayoria de personas que estaban en primera clase sobrevivieron. La
# mayoria de personas que estaban en tercer clase no sobrevivieron. Y en la
# segunda clase fue equilibrado.
