# Proyecto de Detección de Plagio

### Realizado por:

- **Joaquin Jesus Carmona Blanco**
- **José María Samos Pech**
- **Edier Jair May Pech**

---

## Descripción General

Este proyecto implementa un sistema para la detección de plagio entre documentos de texto utilizando técnicas de procesamiento de lenguaje natural (NLP) y análisis de similitud. El sistema analiza un conjunto de documentos generados automáticamente, realiza una limpieza del texto, genera n-gramas (pares o grupos de palabras consecutivas) y calcula la similitud entre documentos utilizando la métrica de Jaccard.

Los resultados se presentan de manera visual mediante:

1. **Grafos de similitudes**: Para identificar las relaciones más fuertes entre documentos.
2. **Mapa de calor (heatmap)**: Para visualizar las similitudes en forma de matriz.

---

## Características Principales

- **Generación automática de documentos**: Se crean documentos de texto con contenido aleatorio para realizar las pruebas.
- **Limpieza y tokenización del texto**: Se eliminan signos de puntuación y se convierten las palabras a minúsculas para un análisis uniforme.
- **Generación de n-gramas**: Se generan bi-gramas (pares de palabras consecutivas) para analizar patrones en los textos.
- **Cálculo de similitud de Jaccard**: Se mide la similitud entre documentos comparando los n-gramas generados.
- **Visualización de resultados**:
  - **Grafo de similitudes**: Muestra las relaciones más importantes entre documentos.
  - **Mapa de calor**: Representa las similitudes en una matriz visualmente intuitiva.

---

## Objetivo del Proyecto

El objetivo principal es proporcionar una herramienta que permita identificar similitudes entre documentos de texto, lo que puede ser útil en contextos como:

- Detección de plagio académico.
- Análisis de contenido duplicado en bases de datos.
- Comparación de documentos en sistemas de gestión de información.

---

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo del sistema.
- **NLTK**: Para la generación de n-gramas y procesamiento de texto.
- **NetworkX**: Para la creación y visualización de grafos.
- **Matplotlib y Seaborn**: Para la visualización de gráficos y mapas de calor.
- **Pandas**: Para la manipulación de datos tabulares.

---

## Estructura del Proyecto

- **`documentos/`**: Contiene el script para generar documentos de texto (`generador_text.py`) y la carpeta donde se almacenan los documentos generados.
- **`src/`**: Contiene el archivo principal (`main.ipynb`) que realiza el procesamiento de texto, generación de n-gramas y cálculo de similitudes.
- **`resultados/`**: Contiene el archivo (`Resultados.ipynb`) para la visualización de los resultados mediante grafos y mapas de calor.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.

---

**Ejemplo de Uso**
Generación de documentos:

Se generan automáticamente 40 documentos en la carpeta documentos/documentos_generados.
Procesamiento de texto:

- Limpieza y tokenización del texto.
- Generación de bi-gramas.
- Cálculo de similitudes:

**Se calcula la similitud de Jaccard entre los documentos y se almacenan los resultados en resultados/similitudes_ordenadas.json.
Visualización:**

Se genera un grafo que muestra las relaciones más fuertes entre documentos.
Se crea un mapa de calor para visualizar las similitudes en forma de matriz.

# Instrucciones para Ejecutar el Proyecto

## 1. Instalar Dependencias

Antes de ejecutar el proyecto, asegúrate de instalar las dependencias necesarias. Ejecuta el siguiente comando en la terminal desde la raíz del proyecto:

```bash
pip install -r requirements.txt
```

2. Generar Documentos de Prueba
   Si no tienes documentos generados, utiliza el script generador_text.py en la carpeta documentos/ para crear documentos de prueba. Los documentos generados se almacenarán en documentos/documentos_generados/.

3. Procesar los Documentos
   Abre y ejecuta el archivo src/main.ipynb en Jupyter Notebook o cualquier entorno compatible. Este archivo realiza los siguientes pasos:

Limpieza y Tokenización:

Convierte los textos a minúsculas.
Elimina signos de puntuación.
Divide el texto en palabras individuales (tokens).
Generación de N-Gramas:

Genera bi-gramas (pares de palabras consecutivas) o tri-gramas según sea necesario.
Creación de Tabla Hash:

Almacena los n-gramas generados en una tabla hash para su análisis.
Cálculo de Similitud de Jaccard:

Compara los documentos generados y calcula la similitud entre ellos.
Ordenar Similitudes:

Usa el algoritmo Merge Sort para ordenar las similitudes de mayor a menor.
Guardar Resultados:

Los resultados se guardan en el archivo resultados/similitudes_ordenadas.json.

4. Visualizar Resultados
   Abre y ejecuta el archivo resultados/Resultados.ipynb para visualizar los resultados. Este archivo incluye:

**Créditos
Este proyecto fue desarrollado como parte de un trabajo académico por:**

Joaquin Jesus Carmona Blanco
José María Samos Pech
Edier Jair May Pech
