# 馃搱 Cuadro de mandos personal 馃搳
 

## Objetivo

El objetivo de esta aplicaci贸n es proporcionar un cuadro de mandos personal para mostrar informaci贸n sobre los Pok茅mon. En concreto, permite visualizar informaci贸n relevante de los Pok茅mon como su ataque, defensa, velocidad y estad铆sticas base, adem谩s de permitir filtrarlos por tipo.

## Los datos

Los datos utilizados en esta aplicaci贸n se encuentran en el archivo pokemon.csv, que contiene informaci贸n detallada sobre los Pok茅mon, incluyendo su nombre, tipo, estad铆sticas y habilidades.

## B煤squeda de los datos

Los datos utilizados en esta aplicaci贸n se obtuvieron de Kaggle, una plataforma de an谩lisis de datos en l铆nea. El conjunto de datos en cuesti贸n es "Pokemon with stats", que incluye informaci贸n detallada sobre los Pok茅mon.

## Documentaci贸n de los datos

La documentaci贸n de los datos utilizados en esta aplicaci贸n se encuentra en el archivo README.md del repositorio correspondiente. Este archivo incluye informaci贸n sobre las columnas de los datos y su significado.

## Prepara tu aplicaci贸n.

Para preparar la aplicaci贸n, se utilizaron las bibliotecas de Python pandas, streamlit, altair y seaborn. Para instalar estas bibliotecas, se utiliz贸 el gestor de paquetes de Python pip.

## Carga y an谩lisis de conjunto de dato con pandas

El archivo pokemon.csv se carg贸 en un DataFrame de pandas para su an谩lisis posterior. Las bibliotecas pandas, numpy y seaborn se utilizaron para analizar y visualizar los datos.

## Visualizaci贸n de los datos

Se utiliz贸 la biblioteca altair para crear visualizaciones interactivas de los datos, lo que permite al usuario interactuar con los datos en tiempo real.


## Dise帽a la interacci贸n que van a tener tus datos
 
Los usuarios pueden seleccionar entre varias opciones de visualizaci贸n, como mostrar la lista completa de Pok茅mon, los 10 Pok茅mon con el mayor ataque, los 10 mejores Pok茅mon en general (no legendarios), el Pok茅mon con el mayor ataque de cada tipo, el Pok茅mon con la mayor defensa de cada tipo, el Pok茅mon con la mayor velocidad de cada tipo, el Pok茅mon con el mayor total de estad铆sticas base de cada tipo y el Pok茅mon con el mayor total de estad铆sticas base de cada tipo (excluyendo a los legendarios). Adem谩s, los usuarios pueden filtrar los Pok茅mon por tipo.

## Prepara la aplicaci贸n (cuadro de mandos) con Streamlit

Se importaron las bibliotecas necesarias, incluyendo pandas, streamlit, altair y seaborn.
Se carg贸 el conjunto de datos en un DataFrame de pandas.
Se cre贸 una funci贸n para cada visualizaci贸n, utilizando la biblioteca altair para crear gr谩ficos interactivos.
Se cre贸 una barra lateral que permite a los usuarios seleccionar entre las diferentes visualizaciones y filtrar los Pok茅mon por tipo.
Se agregaron gr谩ficos adicionales utilizando la biblioteca seaborn para mostrar la distribuci贸n de las estad铆sticas base de los Pok茅mon.
Se utiliz贸 la funci贸n st.beta_set_page_config para personalizar la apariencia de la aplicaci贸n.
Finalmente, se utiliz贸 la funci贸n st.streamlit_chart para mostrar las visualizaciones en la aplicaci贸n.

## Publica la aplicaci贸n.
https://pinilla155-streamlit-2---cuadro-de-mandos-personal-p-app-n4jr2u.streamlit.app/
