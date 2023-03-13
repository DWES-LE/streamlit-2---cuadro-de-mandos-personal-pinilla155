# 📈 Cuadro de mandos personal 📊
 

## Objetivo

El objetivo de esta aplicación es proporcionar un cuadro de mandos personal para mostrar información sobre los Pokémon. En concreto, permite visualizar información relevante de los Pokémon como su ataque, defensa, velocidad y estadísticas base, además de permitir filtrarlos por tipo.

## Los datos

Los datos utilizados en esta aplicación se encuentran en el archivo pokemon.csv, que contiene información detallada sobre los Pokémon, incluyendo su nombre, tipo, estadísticas y habilidades.

## Búsqueda de los datos

Los datos utilizados en esta aplicación se obtuvieron de Kaggle, una plataforma de análisis de datos en línea. El conjunto de datos en cuestión es "Pokemon with stats", que incluye información detallada sobre los Pokémon.

## Documentación de los datos

La documentación de los datos utilizados en esta aplicación se encuentra en el archivo README.md del repositorio correspondiente. Este archivo incluye información sobre las columnas de los datos y su significado.

## Prepara tu aplicación.

Para preparar la aplicación, se utilizaron las bibliotecas de Python pandas, streamlit, altair y seaborn. Para instalar estas bibliotecas, se utilizó el gestor de paquetes de Python pip.

## Carga y análisis de conjunto de dato con pandas

El archivo pokemon.csv se cargó en un DataFrame de pandas para su análisis posterior. Las bibliotecas pandas, numpy y seaborn se utilizaron para analizar y visualizar los datos.

## Visualización de los datos

Se utilizó la biblioteca altair para crear visualizaciones interactivas de los datos, lo que permite al usuario interactuar con los datos en tiempo real.


## Diseña la interacción que van a tener tus datos
 
Los usuarios pueden seleccionar entre varias opciones de visualización, como mostrar la lista completa de Pokémon, los 10 Pokémon con el mayor ataque, los 10 mejores Pokémon en general (no legendarios), el Pokémon con el mayor ataque de cada tipo, el Pokémon con la mayor defensa de cada tipo, el Pokémon con la mayor velocidad de cada tipo, el Pokémon con el mayor total de estadísticas base de cada tipo y el Pokémon con el mayor total de estadísticas base de cada tipo (excluyendo a los legendarios). Además, los usuarios pueden filtrar los Pokémon por tipo.

## Prepara la aplicación (cuadro de mandos) con Streamlit

Se importaron las bibliotecas necesarias, incluyendo pandas, streamlit, altair y seaborn.
Se cargó el conjunto de datos en un DataFrame de pandas.
Se creó una función para cada visualización, utilizando la biblioteca altair para crear gráficos interactivos.
Se creó una barra lateral que permite a los usuarios seleccionar entre las diferentes visualizaciones y filtrar los Pokémon por tipo.
Se agregaron gráficos adicionales utilizando la biblioteca seaborn para mostrar la distribución de las estadísticas base de los Pokémon.
Se utilizó la función st.beta_set_page_config para personalizar la apariencia de la aplicación.
Finalmente, se utilizó la función st.streamlit_chart para mostrar las visualizaciones en la aplicación.

## Publica la aplicación.
https://pinilla155-streamlit-2---cuadro-de-mandos-personal-p-app-n4jr2u.streamlit.app/
