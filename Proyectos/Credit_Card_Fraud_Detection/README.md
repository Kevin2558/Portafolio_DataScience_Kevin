# Detección de Fraude en Transacciones con Tarjeta de Crédito

## Descripción General

Este proyecto se enfoca en la detección de transacciones fraudulentas con tarjeta de crédito utilizando un dataset real anonimizado. El principal desafío abordado fue el desequilibrio severo de clases (muy pocas transacciones fraudulentas en comparación con las legítimas), y se exploraron técnicas para manejarlo y construir modelos predictivos robustos.

## Dataset

* **Nombre del Dataset:** Credit Card Fraud Detection
* **Fuente:** [Enlace a Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* **Descripción Breve:** Contiene transacciones con tarjeta de crédito en septiembre de 2013 por titulares de tarjetas europeas. El dataset tiene 284,807 transacciones, de las cuales solo 492 (0.172%) son fraudulentas. Las características son resultados de una transformación PCA, excepto 'Time' y 'Amount'. La variable objetivo es 'Class' (0 para legítimo, 1 para fraude).

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1.  Analizar y comprender el desequilibrio de clases inherente al dataset de fraude.
2.  Aplicar técnicas de reducción de dimensionalidad (si se considera necesario para visualización o eficiencia).
3.  Implementar y evaluar modelos de clasificación binaria capaces de identificar transacciones fraudulentas.
4.  Explorar estrategias para manejar el desequilibrio de clases, como el ajuste de pesos de clase o el submuestreo/sobremuestreo (aunque el notebook original no lo muestra explícitamente, es un objetivo común para este dataset).
5.  Evaluar el rendimiento de los modelos utilizando métricas apropiadas para datasets desequilibrados (Precision, Recall, F1-Score, Curva ROC/AUC).

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos (EDA):** Se analizaron las distribuciones de las características 'Time' y 'Amount' en relación con las clases. Se confirmó el severo desequilibrio de clases.
2.  **Preprocesamiento de Datos:**
    * La columna 'Time' fue explorada, pero no se transformó explícitamente si no se consideró relevante para el modelo.
    * La columna 'Amount' fue escalada utilizando `StandardScaler` debido a su rango variable.
3.  **Reducción de Dimensionalidad:** Dado que las características V1-V28 ya son el resultado de una transformación PCA, no se aplicó una reducción de dimensionalidad adicional. Sin embargo, se realizó un análisis exploratorio de estas características.
4.  **Modelado:** Se entrenaron los siguientes modelos para clasificación binaria:
    * Regresión Logística
    * Random Forest Classifier
    * SMOTE   
5.  **Evaluación:** El rendimiento de los modelos se evaluó principalmente utilizando métricas como Precision, Recall y F1-Score, ya que la precisión (accuracy) puede ser engañosa en datasets desequilibrados.

## Resultados y Conclusiones Clave

* **Desequilibrio de Clases:** El desequilibrio de clases fue un factor crítico. Modelos entrenados sin estrategias de manejo de desequilibrio tendían a tener un alto recall para la clase mayoritaria (no fraude) y un bajo recall para la clase minoritaria (fraude).
* **Métricas Relevantes:** El **Recall** para la clase de fraude (capacidad del modelo para identificar todas las transacciones fraudulentas) fue una métrica clave, ya que minimizar los falsos negativos es crucial en la detección de fraude. El **Precision** (minimizar falsos positivos) también fue importante para evitar rechazos innecesarios de transacciones legítimas.
* **Rendimiento del Modelo:** El modelo Random Forest mostró un balance prometedor entre Precision y Recall. Se logró un 67% de Recall para transacciones fraudulentas con una precisión razonable de 67%.
* **Desafíos:** Identificar un balance óptimo entre falsos positivos y falsos negativos es un desafío inherente a este problema. La optimización se realizó en base a maximizar tanto precision como recall de los casos fraudulentos.

## Tecnologías y Librerías Utilizadas

* Python 3.x
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`
* `seaborn`
* `imblearn`

## Autor

* **Kevin Ortiz, Almendra Orellana, Jorge Pastene**
* [GitHub](https://github.com/Kevin2558)
* [LinkedIn](https://www.linkedin.com/in/kevin-ortiz-collao-16376a275/)
