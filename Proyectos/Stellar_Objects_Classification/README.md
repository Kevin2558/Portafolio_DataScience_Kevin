# Clasificación de objetos estelares en catálogos astronómicos.

## Descripción General

Este proyecto busca desarrollar un modelo de clasificación que sea capaz de identificar y categorizar diferentes tipos de objetos estelares (ej. estrellas, galaxias, cuásares) utilizando características numéricas extraídas del catálogo astronómico SDSS.

## Dataset

* **Nombre del Dataset:** SDSS Data
* **Fuente:** [Enlace de Kaggle al dataset](https://www.kaggle.com/code/farazrahman/predicting-star-galaxy-quasar-with-svm)
* **Descripción Breve:** Este dataset consiste en una colección de 10.000 observaciones del espacio tomadas por la Sloan Digital Sky Survey. Cada observación está descrita por 17 características y una variable objetivo la cual identifica la observación como una estrella, una galaxia o un quásar.

## Objetivos generales del proyecto

El proyecto se enfoca principalmente en construir un modelo de clasificación de objetos estelares en ayuda de aficionados por la astronomía con y sin experiencia que deseen identificar, a través de magnitudes físicas y/o imágenes, lo que observan en el cielo.

El proyecto se separa en dos aristas. Primero analizaremos las magnitudes fotométricas de los objetos en distintos rangos de longitud de onda y luego analizaremos imágenes de estrellas y galaxias. Estos dos enfoques buscan comprender un gran número de personas, en distinto niveles de conocimiento de astronomía.

## Objetivos técnicos del proyecto

Los principales objetivos de este proyecto fueron:

1. Realizar un análisis exploratorio del dataset SDSS, evaluando la distribución de clases, presencia de outliers y relaciones entre características.
2. Aplicar técnicas de preprocesamiento de datos, incluyendo normalización, tratamiento de datos faltantes y balanceo de clases (si son necesarias). Para el caso de las imágenes aplicar técnicas de preprocesamiento de imágenes, antes de entrar a la red neuronal.
3. Visualizar los datos en espacios de baja dimensión (2D o 3D) para identificar agrupamientos y facilitar el entendimiento de la estructura del dataset. 
4. Diseñar, entrenar y evaluar distintos modelos de clasificación, medir su rendimiento y compararlos. Diseñar, entrenar y evaluar una CNN para clasificar imágenes de los objetos estelares.
5. Interpretar el proceso de decisión de cada uno de los modelos, integrando visualizaciones de sus fronteras de decisión.
6. Visualizar las imágenes de los objetos estelares e incorporar imágenes externas al dataset para evaluar la clasifición de la CNN.
7. Sintetizar los hallazgos, discutir los resultados de cada proceso y decicidir el modelo más atractivo a utilizar.

## Metodología

### Parte 1

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

### Parte 2

El proceso seguido en esta parte del proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos (EDA):** Se cargaron las imágenes del dataset y se visualizó un ejemplo de cada clase (estrella y galaxia) para comprender la naturaleza de los datos de imagen.
2.  **Preprocesamiento de Datos:** Se aplicaron transformaciones a las imágenes, incluyendo redimensionamiento, conversión a tensor y normalización. Posteriormente, el dataset fue dividido en conjuntos de entrenamiento y prueba, y se crearon DataLoaders para manejar la carga de datos en mini-batches.
3.  **Modelado:** Se entrenaron dos modelos de Redes Neuronales Convolucionales (CNN):
    *   Una CNN simple diseñada desde cero.
    *   Un modelo pre-entrenado (ResNet-18) adaptado mediante Fine-Tuning.
4.  **Visualización:** Se utilizaron técnicas de visualización como la visualización de predicciones en un lote de imágenes y Grad-CAM para entender qué partes de las imágenes influyen en las decisiones del modelo.
5.  **Evaluación:** El rendimiento de los modelos fue evaluado utilizando métricas como Precisión, Recall, F1-score y Matrices de Confusión para comparar el desempeño de la CNN simple y el modelo basado en Transfer Learning.

## Resultados y Conclusiones Clave

### Parte 1

* **Características importantes:** El dataset posee 18 variables y en general no aportan gran información para este proyecto, por lo que se toma en cuenta las variables u, g, r, i, z y redshift. 
* **Outliers:** El dataset posee un porcentaje considerable de outliers, por lo que se decide aplicar RobustScaler para evitar que conlleven errores al momento de entrenar los modelos.
* **Modelado:** Los modelos k-NN, RF y XGB tienden a tener fronteras de decisión más lineales, unas más complejas que otras y los modelos SVC y MLP tienden a tener fronteras de decisión más curvas y suaves. Tomando en cuenta las métras antes mencionadas los mejores modelos obtenidos fueron XGBoost y MLP (100,50,25), donde XGBoost brilla por su rendimiento y MLP (100,50,25) por su entendimiento profundo de las clases.
* **Optimización:** Se tomaron los dos mejores modelos y se procede a optimizar sus hiperparámetros en busca del mejor modelo. Se determina que en terminos de rendimiento XGBoost sigue siendo mejor pero alcanza a igual la precisión de MLP.
* **Desafios:** Ante la ventaja a nivel de precisión de MLP, se espera proceder a utilizar redes neuronales convolucionales para tratamiento de imágenes de objetos estelares y así no necesitar las variables fotométricas para clasificar.

### Parte 2

*   **Dataset:** Se utilizó un dataset de imágenes de objetos estelares (estrellas y galaxias) capturadas por el telescopio de 1.3 metros del observatorio ARIES, en Nainnital, India.
*   **Preprocesamiento:** Las imágenes fueron redimensionadas, convertidas a tensores y normalizadas. El dataset se dividió en conjuntos de entrenamiento y prueba, y se crearon DataLoaders para la carga de datos.
*   **Modelado:** Se entrenaron dos modelos CNN: una CNN simple diseñada desde cero y un modelo pre-entrenado (ResNet-18) con Fine-Tuning.
*   **Visualización:** La visualización con Grad-CAM mostró que la CNN simple se enfoca en los cambios de luminosidad centrales, mientras que ResNet-18 es más sensible a las variaciones de luminosidad a lo largo del eje horizontal.
*   **Evaluación:** La CNN simple obtuvo una mayor precisión global (90%) en comparación con ResNet-18 (79%), con mejores métricas de precisión, recall y f1-score para ambas clases. Esto sugiere que la arquitectura simple fue más adecuada para este dataset específico.
*   **Desafíos:** Aunque la CNN simple tuvo un buen rendimiento, se podrían explorar técnicas de aumento de datos más robustas y arquitecturas más recientes para mejorar la generalización en trabajos futuros.

## Tecnologías y Librerías Utilizadas

Este proyecto utilizó principalmente Python y las siguientes librerías:

**Parte 1 (Clasificación con Magnitudes Fotométricas):**

*   **pandas**
*   **numpy**
*   **matplotlib.pyplot** 
*   **seaborn**
*   **sklearn (scikit-learn):**
    *   `model_selection`
    *   `preprocessing`
    *   `metrics`
    *   `manifold`
    *   `neural_network`
    *   `ensemble`
    *   `neighbors`
    *   `svm`
*   **imblearn (imbalanced-learn):**
    *   `over_sampling`
    *   `pipeline`
*   **xgboost** 
*   **scipy**

**Parte 2 (Clasificación con Imágenes):**

*   **torch** 
*   **torch.nn**
*   **torch.nn.functional** 
*   **matplotlib.pyplot** 
*   **PIL (Pillow)** 
*   **torchvision:**
    *   `transforms`
    *   `datasets`
    *   `utils`
    *   `models`
*   **requests**
*   **io** 
*   **torch.utils.data:**
    *   `DataLoader`
*   **tqdm** 
*   **pytorch-grad-cam** 
*   **kagglehub**
   
## Autor

* **Almendra Orellana, Kevin Ortiz, Jorge Pastene**
* [GitHub](https://github.com/Kevin2558)
* [LinkedIn](https://www.linkedin.com/in/kevin-ortiz-collao-16376a275/)
