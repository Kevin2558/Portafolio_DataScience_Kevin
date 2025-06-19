# Predicción de Eficiencia Energética en Edificios

## Descripción General

Este proyecto aborda la tarea de predecir la eficiencia energética de edificios residenciales, específicamente las cargas de calefacción y refrigeración, basándose en diversas características arquitectónicas. El objetivo fue desarrollar modelos de regresión capaces de estimar con precisión estas cargas, lo que tiene implicaciones importantes para el diseño de edificios sostenibles.

## Dataset

* **Nombre del Dataset:** Energy Efficiency Dataset
* **Fuente:** [Enlace a UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/242/energy+efficiency)
* **Descripción Breve:** El dataset contiene 768 muestras de 8 características arquitectónicas (ej., área de superficie, orientación, área de acristalamiento, altura) y dos variables de salida continuas: carga de calefacción (Heating Load) y carga de refrigeración (Cooling Load).

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1.  Cargar y explorar un dataset que describe las propiedades arquitectónicas de edificios.
2.  Aplicar PCA para la reducción de dimensionalidad, con el fin de ver si la reducción de dimensionalidad siempre responde a una ventaja o no.
3.  Desarrollar y evaluar modelos de regresión para predecir las cargas de calefacción y refrigeración.
4.  Comparar el rendimiento de los modelos con y sin la aplicación de PCA.

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos (EDA):** Se cargó el dataset. Se realizaron análisis para entender las relaciones entre las características de entrada y las variables de salida (cargas de calefacción/refrigeración).
2.  **Preprocesamiento de Datos:** Las características numéricas de entrada se escalaron utilizando `StandardScaler` para asegurar que los modelos no se vieran sesgados por las diferentes escalas de las variables.
3.  **Reducción de Dimensionalidad:** Se aplicó PCA para transformar las 8 características originales a un número menor de componentes principales, buscando preservar la mayor parte de la varianza.
4.  **Modelado:** Se entrenaron los siguientes modelos de regresión para predecir tanto la carga de calefacción como la de refrigeración:
    * Regresión Lineal
    * Ridge Regression
    * Random Forest Regressor
5.  **Evaluación:** El rendimiento de los modelos fue evaluado utilizando métricas de regresión clave: MAE (Error Absoluto Medio), RMSE (Raíz del Error Cuadrático Medio) y R² (Coeficiente de Determinación).

## Resultados y Conclusiones Clave

* **Rendimiento del Modelo:** Los modelos de regresión, particularmente Random Forest, mostraron un rendimiento muy sólido en la predicción de las cargas de calefacción y refrigeración. Se lograron valores de R² superiores a 97% para ambas variables objetivo con Random Forest.
* **Impacto de PCA:** La aplicación de PCA representó una desventaja en comparación con el uso de todas las características originales. Por ejemplo, en la regresión lineal al aplicarlar PCA a las variables, el valor de R² disminuyó en un 20% y el tiempo de ejecución fue el mismo.
* **Potencial:** Los modelos desarrollados pueden servir como una herramienta útil para ingenieros y arquitectos en las fases iniciales de diseño para estimar el consumo energético y optimizar el diseño.

## Tecnologías y Librerías Utilizadas

* Python 3.x
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`
* `seaborn`

## Autor

* **Kevin Ortiz, Almendra Orellana, Jorge Pastene**
* [Tu Perfil de GitHub](https://github.com/Kevin2558)
* [Tu Perfil de LinkedIn](https://www.linkedin.com/in/kevin-ortiz-collao-16376a275/)
