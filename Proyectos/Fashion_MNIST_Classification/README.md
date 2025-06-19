# Clasificación de Imágenes de Moda con Fashion MNIST

## Descripción General

Este proyecto se centra en la clasificación de imágenes de artículos de moda (camisetas, pantalones, zapatillas, etc.) utilizando el dataset Fashion MNIST. El objetivo principal fue explorar la aplicación de técnicas de reducción de dimensionalidad como PCA y evaluar el rendimiento de diferentes modelos de clasificación en un problema de visión por computadora simplificado.

## Dataset

* **Nombre del Dataset:** Fashion MNIST
* **Fuente:** [Enlace a Kaggle Fashion MNIST Dataset](https://www.kaggle.com/datasets/zalando-research/fashionmnist) o [Enlace al original de Zalando](https://github.com/zalandoresearch/fashion-mnist)
* **Descripción Breve:** Un dataset de 70,000 imágenes en escala de grises de 28x28 píxeles de 10 categorías de artículos de moda. Incluye 60,000 imágenes para entrenamiento y 10,000 para prueba. Es un reemplazo directo de MNIST para benchmarks de Machine Learning.

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1.  Cargar, explorar y visualizar imágenes del dataset Fashion MNIST.
2.  Aplicar PCA para reducir la dimensionalidad de las imágenes y observar su impacto en la representación visual y el entrenamiento.
3.  Desarrollar y evaluar modelos de clasificación multiclase (como Regresión Logística y SVM) en los datos originales y en los datos transformados con PCA.
4.  Comparar el rendimiento (Accuracy, Precision, Recall, F1-Score) de los modelos con y sin reducción de dimensionalidad.

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos:** Se cargaron las imágenes y etiquetas. Se visualizaron ejemplos de cada clase para comprender el dataset.
2.  **Preprocesamiento de Datos:** Las imágenes se aplanaron (flatten) de 28x28 a vectores de 784 píxeles y se normalizaron los valores de píxeles al rango [0, 1].
3.  **Reducción de Dimensionalidad:** Se aplicó PCA para reducir la dimensionalidad a un número de componentes que explicara una alta proporción de la varianza total (ej., 95%). Esto también se utilizó para visualizar los datos en 2D.
4.  **Modelado:** Se entrenaron los siguientes modelos:
    * Regresión Logística
    * Support Vector Machine
    * K Nearest Neighbors
5.  **Evaluación:** El rendimiento de los modelos fue evaluado utilizando métricas comunes de clasificación: Accuracy, Precision, Recall y F1-Score.

Nota: Los modelos se entrenaron tanto en los datos originales como en los datos transformados por PCA.

## Resultados y Conclusiones Clave

* **Reducción de Dimensionalidad:** PCA fue efectivo para reducir la dimensionalidad del dataset, permitiendo una representación más compacta sin una pérdida significativa de información para la clasificación. Por ejemplo, 256 componentes principales capturaron más del 95% de la varianza.
* **Rendimiento del Modelo:** El modelo k-NN consistentemente obtuvo el mejor rendimiento en ambos escenarios (con y sin PCA), alcanzando una precisión (accuracy) de aproximadamente 87% en los datos de prueba.
* **Impacto de PCA en el Rendimiento:** La aplicación de PCA ligeramente mejoró el rendimiento general de los modelos, pero redujo significativamente el tiempo de entrenamiento.
* **Clases Desafiantes:** Se observó que algunas clases, como camisas y poleras, eran más difíciles de distinguir para los modelos, resultando en menores puntuaciones de precisión/recall para esas categorías.

## Tecnologías y Librerías Utilizadas

* Python 3.x
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`
* `seaborn`

## Autor

* **Kevin Ortiz**
* [GitHub](https://github.com/Kevin2558)
* [LinkedIn](https://www.linkedin.com/in/tu-perfil-linkedin/)
