# Introducción al Riesgo de Liquidez

## Descripción General

Este proyecto aborda el análisis y monitoreo del riesgo de liquidez en una institución financiera, centrándose en las métricas clave definidas por Basilea III y la CMF chilena. Utiliza datasets artificiales para ilustrar los conceptos y cálculos de HQLA, LCR, GAP de Liquidez y NSFR. El objetivo principal fue introducir los conceptos del riesgo de liquidez, poner en práctica sus cálculos y generar una base sólida en el tema a través de la construcción de una herramienta conceptual.

## Dataset

* **Nombre del Dataset:** Datasets Artificiales de HQLA, Flujos de Caja, Activos y Pasivos.
* **Fuente:** Datos creados artificialmente para fines demostrativos.
* **Descripción Breve:** Consiste en cuatro dataset: uno para Activos Líquidos de Alta Calidad (HQLA) con nombre, nivel, monto y haircut; otro para Flujos de Caja con tramos de vencimiento, entradas y salidas; y dos más para Activos y Pasivos con nombre, monto y factores RSF/ASF respectivamente.

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1. Definir y comprender el concepto de Activos Líquidos de Alta Calidad (HQLA) según Basilea III.
2. Calcular el Ratio de Cobertura de Liquidez (LCR) basándose en el stock de HQLA y las salidas netas esperadas.
3. Analizar el GAP de Liquidez por tramos de vencimiento para identificar descalces en los flujos de caja.
4. Calcular el Ratio de Fondeo Estable Neto (NSFR) utilizando los Fondos Estables Disponibles (ASF) y los Requerimientos de Fondos Estables (RSF).
5. Simular escenarios de estrés para evaluar el impacto en las métricas de liquidez.
6. Diseñar e implementar un Plan de Contingencia de Liquidez (CFP) para mitigar los efectos de los escenarios de estrés.
7. Visualizar y comparar los resultados de las métricas bajo diferentes escenarios.

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1. **Definición de HQLA:** Se definieron los HQLA, sus niveles y el concepto de haircut, creando un dataset artificial para representarlos.
2. **Cálculo de LCR:** Se explicó la fórmula del LCR y se calculó utilizando el stock de HQLA neto y salidas/entradas esperadas (con una función para entrada interactiva de datos).
3. **Análisis de GAP de Liquidez:** Se creó un dataset de flujos de caja por tramos, se calculó el GAP neto y acumulado, y se definió una función para clasificar el riesgo asociado a cada tramo.
4. **Cálculo de NSFR:** Se definieron los conceptos de activos y pasivos, se explicó el NSFR y se calculó utilizando datasets artificiales de activos y pasivos ponderados por sus factores RSF y ASF.
5. **Simulación de Escenarios de Estrés y CFP:** Se definieron los escenarios de estrés, se crearon escenarios artificiales (fuga de depósitos, cambios en flujos) modificando los datasets base, se calculó el impacto en las métricas y se aplicó un CFP con ajustes en HQLA y ASF. Se creó una función para automatizar el cálculo y la presentación de resultados por escenario.
6. **Visualización:** Se generaron gráficos comparativos del LCR y NSFR a través de los escenarios (Base, Estrés, Estrés + CFP) y un gráfico de barras para visualizar el GAP acumulado bajo estrés.

## Resultados y Conclusiones Clave

* El cálculo de HQLA neto demostró la cantidad de activos líquidos disponibles después de aplicar haircuts, cumpliendo con los requisitos de Nivel 1 y Nivel 2A/B.
* El LCR base cumplió ampliamente el umbral del 100% establecido por la CMF, indicando suficiente liquidez a corto plazo en condiciones normales.
* El análisis de GAP de Liquidez reveló déficits acumulados en todos los tramos, señalando una exposición al riesgo de iliquidez en el mediano y largo plazo según los supuestos del dataset artificial.
* El NSFR base superó el umbral del 100% (y el 90% actual de la CMF), mostrando una estructura de fondeo estable adecuada para los activos a largo plazo.
* El escenario de estrés simulado (fuga de depósitos y cambios en flujos) impactó negativamente ambas métricas, haciendo que el LCR y el NSFR incumplieran los umbrales normativos.
* La aplicación del Plan de Contingencia de Liquidez (CFP), mediante una línea de crédito y venta rápida de activos, permitió que tanto el LCR como el NSFR volvieran a cumplir los umbrales bajo el escenario de estrés, demostrando la efectividad de las medidas de mitigación.
* La visualización comparativa ilustró claramente el deterioro de las métricas bajo estrés y su recuperación tras la aplicación del CFP. 

## Tecnologías y Librerías Utilizadas

* Python 3.11
* `pandas`
* `matplotlib`
* `seaborn`

## Autor

* **Kevin Ortiz**
* [GitHub](https://github.com/Kevin2558/Portafolio_DataScience)
* [LinkedIn](https://www.linkedin.com/in/kevin-ortiz-collao/)
