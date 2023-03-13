import pandas as pd
import streamlit as st
import altair as alt
import seaborn as sns
import random

# cargar el archivo CSV en un DataFrame
df = pd.read_csv('pokemon.csv')

# opciones de visualización de Pokémon
options = [
    'Lista completa de Pokémon',
    'Los 10 Pokémon con el mayor ataque',
    'Los 10 mejores Pokémon en general (no legendarios)',
    'El Pokémon con el mayor ataque de cada tipo',
    'El Pokémon con la mayor defensa de cada tipo',
    'El Pokémon con la mayor velocidad de cada tipo',
    'El Pokémon con el mayor total de estadísticas base de cada tipo',
    'El Pokémon con el mayor total de estadísticas base de cada tipo (excluyendo a los legendarios)'
]

# opción seleccionada por el usuario
option = st.sidebar.selectbox('Selecciona una opción', options)

# mostrar la lista completa de Pokémon
if option == 'Lista completa de Pokémon':
    st.write('Lista completa de Pokémon')
    st.write(df)

# mostrar los 10 Pokémon con el mayor ataque
elif option == 'Los 10 Pokémon con el mayor ataque':
    st.write('Los 10 Pokémon con el mayor ataque')
    st.write(df[['name', 'attack']].sort_values('attack', ascending=False).head(10))
    

# mostrar los 10 mejores Pokémon en general (no legendarios)
elif option == 'Los 10 mejores Pokémon en general (no legendarios)':
    st.write('Los 10 mejores Pokémon en general (no legendarios)')
    st.write(df[df['is_legendary'] == False][['name', 'base_total']].sort_values('base_total', ascending=False).head(10))

# mostrar el Pokémon con el mayor ataque de cada tipo
elif option == 'El Pokémon con el mayor ataque de cada tipo':
    # agrupar por tipo y obtener el Pokémon con el mayor ataque de cada tipo
    max_attack_by_type = df.loc[df.groupby('type1')['attack'].idxmax()]
    st.write('El Pokémon con el mayor ataque de cada tipo')
    st.write(max_attack_by_type[['type1', 'name', 'attack']])

# mostrar el Pokémon con la mayor defensa de cada tipo
elif option == 'El Pokémon con la mayor defensa de cada tipo':
    # agrupar por tipo y obtener el Pokémon con la mayor defensa de cada tipo
    max_defense_by_type = df.loc[df.groupby('type1')['defense'].idxmax()]
    st.write('El Pokémon con la mayor defensa de cada tipo')
    st.write(max_defense_by_type[['type1', 'name', 'defense']])

# mostrar el Pokémon con la mayor velocidad de cada tipo
elif option == 'El Pokémon con la mayor velocidad de cada tipo':
    # agrupar por tipo y obtener el Pokémon con la mayor velocidad de cada tipo
    max_speed_by_type = df.loc[df.groupby('type1')['speed'].idxmax()]
    st.write('El Pokémon con la mayor velocidad de cada tipo')
    st.write(max_speed_by_type[['type1', 'name', 'speed']])

# mostrar el Pokémon con el mayor total de estadísticas base de cada tipo
elif option == 'El Pokémon con el mayor total de estadísticas base de cada tipo':
    # agrupar por tipo y obtener el Pokémon con el mayor total de estadísticas base de cada tipo
    max_base_total_by_type = df.loc[df.groupby('type1')['base_total'].idxmax()]
    st.write('El Pokémon con el mayor total de estadísticas base de cada tipo')
    st.write(max_base_total_by_type[['type1', 'name', 'base_total']])

# mostrar el Pokémon con el mayor total de estadísticas base de cada tipo (excluyendo a los legendarios)
elif option == 'El Pokémon con el mayor total de estadísticas base de cada tipo (excluyendo a los legendarios)':
    # filtrar los Pokémon legendarios
    df = df[df['is_legendary'] == False]
    # agrupar por tipo y obtener el Pokémon con el mayor total de estadísticas base de cada tipo
    max_base_total_by_type = df.loc[df.groupby('type1')['base_total'].idxmax()]
    st.write('El Pokémon con el mayor total de estadísticas base de cada tipo (excluyendo a los legendarios)')
    st.write(max_base_total_by_type[['type1', 'name', 'base_total']])

# filtrar pokemons por tipo 
if st.sidebar.checkbox('Filtrar por tipo'):
     # obtener los tipos de Pokémon
    types = df['type1'].unique()
    # opción seleccionada por el usuario
    type = st.sidebar.selectbox('Selecciona un tipo', types)
    # filtrar los Pokémon por el tipo seleccionado
    filtered_df = df[df['type1'] == type]
    # mostrar el nombre y el tipo de los Pokémon filtrados
    st.write('Pokémon de tipo ' + type)
    st.write(filtered_df[['name', 'type1', 'type2', 'abilities']])

# contar la cantidad de Pokémon de cada tipo
poke_count = df['type1'].value_counts()

# crear el gráfico de barras con Altair
st.write('Cantidad de Pokémon de cada tipo')
bar_chart = alt.Chart(poke_count.reset_index()).mark_bar().encode(
    x='index',
    y='type1',
    tooltip=['index', 'type1']
)

# mostrar el gráfico de barras en la aplicación
st.altair_chart(bar_chart, use_container_width=True)

# crear el gráfico de dispersión con Altair
scatter_plot = alt.Chart(df).mark_circle().encode(
    x='attack',
    y='defense',
    tooltip=['name', 'type1', 'type2', 'base_total']
)

# mostrar el gráfico de dispersión en la aplicación
st.write('Tabla de dispersión Ataque vs Defensa')
st.altair_chart(scatter_plot, use_container_width=True)

# pedir al usuario que ingrese la estadística base mínima
base_total_min = st.sidebar.slider('Estadística base mínima', min_value=0, max_value=780, step=10, value=0)

# filtrar los Pokémon por la estadística base mínima
st.write('Pokémon según la cantidad de estadísticas base mínima ')
filtered_df = df[df['base_total'] >= base_total_min]

# mostrar el nombre, tipo y estadísticas base de los Pokémon filtrados
st.write(filtered_df[['name', 'type1', 'type2', 'base_total', 'attack', 'defense', 'hp', 'speed']])

# pedir al usuario que ingrese el nombre del Pokémon a buscar
pokemon_name = st.sidebar.text_input('Nombre del Pokémon')

# filtrar los Pokémon por el nombre ingresado
filtered_df = df[df['name'].str.contains(pokemon_name, case=False)]

# mostrar el nombre, tipo y estadísticas base de los Pokémon filtrados
st.write('Pokémon según el nombre ingresado')
st.write(filtered_df[['name', 'type1', 'type2', 'base_total', 'attack', 'defense', 'hp', 'speed']])


# opciones para el histograma
hist_options = {
    'hp': 'Puntos de vida (HP)',
    'attack': 'Ataque',
    'defense': 'Defensa',
    'sp_attack': 'Ataque especial',
    'sp_defense': 'Defensa especial',
    'speed': 'Velocidad',
    'base_total': 'Total de estadísticas base'
}

# opción seleccionada por el usuario
selected_hist = st.sidebar.selectbox('Selecciona una opción para el histograma', list(hist_options.keys()))

# crear histogramas de las estadísticas base de los Pokémon
sns.set(style='darkgrid')
fig = sns.histplot(df, x=selected_hist, bins=20, kde=True)
st.write('Histograma de ' + hist_options[selected_hist])
st.pyplot(fig.figure)


# crear un selector para que el usuario pueda elegir sus Pokémon
st.sidebar.title('Selecciona tu equipo')
selected_pokemon = st.sidebar.multiselect('Selecciona hasta 6 Pokémon', df['name'])

# mostrar las estadísticas base totales del equipo seleccionado
if selected_pokemon:
    selected_pokemon_df = df[df['name'].isin(selected_pokemon)]
    base_total = selected_pokemon_df['base_total'].sum()
    st.write('Estadísticas base totales del equipo seleccionado:', base_total)

    # permitir que el usuario seleccione un tipo de oponente
    st.sidebar.title('Selecciona el tipo de oponente')
    opponent_type = st.sidebar.selectbox('Selecciona el tipo de oponente', df['type1'].unique())

    # seleccionar al azar un equipo de Pokémon que sea efectivo contra el tipo del oponente seleccionado
    opponent_pokemon_df = df[df['type1'] == opponent_type].sample(n=6, replace=True)

    # mostrar las estadísticas base totales del equipo del oponente seleccionado
    opponent_base_total = opponent_pokemon_df['base_total'].sum()
    st.write('Estadísticas base totales del equipo del oponente:', opponent_base_total)

    # comparar las estadísticas base totales de ambos equipos y mostrar al usuario el equipo que tiene más potencial de batalla
    if base_total > opponent_base_total:
        st.write('¡Tu equipo tiene más potencial de batalla!')
    elif base_total < opponent_base_total:
        st.write('¡El equipo del oponente tiene más potencial de batalla!')
    else:
        st.write('Ambos equipos tienen el mismo potencial de batalla.')

    # mostrar una simulación de batalla entre ambos equipos y mostrar el resultado
    st.title('Simulación de batalla')
    st.write('¡La batalla está por comenzar!')
    st.write(selected_pokemon_df['name'].tolist(), 'vs', opponent_pokemon_df['name'].tolist())

    # determinar el equipo ganador al azar
    winner = random.choice(['Tu equipo', 'El equipo del oponente'])
    st.write(winner, 'ha ganado la batalla!')






