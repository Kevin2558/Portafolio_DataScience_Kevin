# 08 - Implementación y Despliegue de Modelos

Esta sección muestra cómo llevar un modelo de Machine Learning desde su entrenamiento hasta su implementación básica en producción.

## Contenido

- **Entrenamiento y Pipeline**
   - Uso de `Pipeline` de Scikit-learn para encapsular preprocesamiento y modelo.

- **Serialización del Modelo**
   - Guardado del modelo con `joblib` para facilitar su reutilización.

- **Predicción con Nuevos Datos**
   - Ejemplo de cómo cargar el modelo y aplicarlo sobre datos nuevos.

El proceso está basado en el dataset de cáncer de mama (`sklearn.datasets.load_breast_cancer`) pero puede adaptarse a cualquier modelo entrenado con Scikit-learn.
