# Clasificación de objetos estelares en catálogos astronómicos.

## Descripción General

Este proyecto busca desarrollar un modelo de clasificación que sea capaz de identificar y categorizar diferentes tipos de objetos estelares (ej. estrellas, galaxias, cuásares) utilizando características numéricas extraídas del catálogo astronómico SDSS.

## Dataset

* **Nombre del Dataset:** SDSS Data
* **Fuente:** [Enlace de Kaggle al dataset](https://www.kaggle.com/code/farazrahman/predicting-star-galaxy-quasar-with-svm)
* **Descripción Breve:** Este dataset consiste en una colección de 10.000 observaciones del espacio tomadas por la Sloan Digital Sky Survey. Cada observación está descrita por 17 características y una variable objetivo la cual identifica la observación como una estrella, una galaxia o un quásar.

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1. Realizar un análisis exploratorio del dataset SDSS, evaluando la distribución de clases, presencia de outliers y relaciones entre características.
2. Aplicar técnicas de preprocesamiento de datos, incluyendo normalización, tratamiento de datos faltantes y balanceo de clases (si son necesarias).
3. Visualizar los datos en espacios de baja dimensión (2D o 3D) para identificar agrupamientos y facilitar el entendimiento de la estructura del dataset.
4. Diseñar, entrenar y evaluar distintos modelos de clasificación, medir su rendimiento y compararlos.
5. Interpretar el proceso de decisión de cada uno de los modelos, integrando visualizaciones de sus fronteras de decisión.
6. Sintetizar los hallazgos, discutir los resultados de cada proceso y decicidir el modelo más atractivo a utilizar.

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos (EDA):** Se analizaron las diferentes características del dataset mostrando su comportamiento, presencia de outliers y correlación entre ellas, se determinaron que características no aportaban información para el modelado y se comprueba el desequilibrio de las clases presentes.
2.  **Preprocesamiento de Datos:** Debido a la presencia de outliers, se aplicar RobustScaler para escalar los datos y debido al desequilibrio de clases se aplicó SMOTE para balancearlas.
3.  **Reducción de Dimensionalidad:** Se utilizó la técnica de reducción de dimensionalidad t-SNE para la visualización 2D de las clases y de las fronteras de decisión de cada uno de los modelos utilizados.
4.  **Modelado:** Se entrenaron y evaluaron varios modelos de Machine Learning, incluyendo:
    * K Nearest Neighbors
    * Support Vector Classifier (RBF)
    * Random Forest
    * Extreme Gradient Boosting
    * Multilayer Perceptron
5.  **Evaluación:** El rendimiento de los modelos fue evaluado utilizando métricas como Precisión, Recall, F1-score y Matrices de Confusión, debido al evidente desequilibrio de las clases.

## Resultados y Conclusiones Clave

* **Características importantes:** El dataset posee 18 variables y en general no aportan gran información para este proyecto, por lo que se toma en cuenta las variables u, g, r, i, z y redshift. 
* **Outliers:** El dataset posee un porcentaje considerable de outliers, por lo que se decide aplicar RobustScaler para evitar que conlleven errores al momento de entrenar los modelos.
* **Modelado:** Los modelos k-NN, RF y XGB tienden a tener fronteras de decisión más lineales, unas más complejas que otras y los modelos SVC y MLP tienden a tener fronteras de decisión más curvas y suaves. Tomando en cuenta las métras antes mencionadas los mejores modelos obtenidos fueron XGBoost y MLP (100,50,25), donde XGBoost brilla por su rendimiento y MLP (100,50,25) por su entendimiento profundo de las clases.
* **Optimización:** Se tomaron los dos mejores modelos y se procede a optimizar sus hiperparámetros en busca del mejor modelo. Se determina que en terminos de rendimiento XGBoost sigue siendo mejor pero alcanza a igual la precisión de MLP.
* **Desafios:** Ante la ventaja a nivel de precisión de MLP, se espera proceder a utilizar redes neuronales convolucionales para tratamiento de fotografías de objetos estelares y así no necesitar las variables fotométricas para clasificar.

## Tecnologías y Librerías Utilizadas

* Python 3
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`
* `seaborn`
* `xgboost`
* `imblearn`

## Autor

* **Kevin Ortiz**
* [GitHub](https://github.com/Kevin2558)
* [LinkedIn](https://www.linkedin.com/in/kevin-ortiz-collao-16376a275/)
