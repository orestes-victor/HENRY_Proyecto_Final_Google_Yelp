# Archivo: deploy_model.py

# Importar las bibliotecas necesarias
import streamlit as st
import pandas as pd

# data = pd.read_parquet('../datasets/data_modelo.parquet')
data = pd.read_parquet('datasets/data_modelo.parquet')

def recomendacion(target: str, rango: int):

    """
    
    """
    if target == 'BIDATING':
        df = data.sort_values(by= 'PREDICTED_RATING_HOTEL', ascending= False)[0:rango]
    elif target == 'por calidad de servicio en la zona':
        df = data.sort_values(by= 'RATING', ascending= False)[0:rango]
    elif target == 'por interaccion comercial y consumo':
        df = data.sort_values(by= 'REVIEW_COUNT', ascending= False)[0:rango]
    elif target == 'por calidad de la competencia':
        df = data.sort_values(by= 'RATING_HOTEL', ascending= False)[0:rango]

    return df.reset_index(drop= True)

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Sistema de Recomendacion de Inversion y Desarrollo Hotelero</h1>", unsafe_allow_html=True)

# Encabezado y descripción
st.write("""
Este es un Sistema de Recomendacion de Inversion y Desarrollo Hotelero, en parte basado en un modelo de Regresion Lineal.
Introduce los parametros para predecir el puntaje.
Ten en cuenta que de acuerdo al criterio que elijas como objetivo, se te dará un resultado basado en ese criterio.
""")

# Nota emergente para guiar al usuario
st.info("Selecciona el criterio objetivo utilizando el siguiente menú desplegable. El criterio objetivo seleccionado dara las recomendaciones de desarrollo y la extensión de la muestra la cantidad de lugares. Ajusta los parámetros según sea necesario y haz clic en 'Recomendar' para obtener el informe.")

# Agrega los selectorbox, sliders, etc para ingresar los valores de los parametros que va a alimentar al modelo
criterio = st.selectbox('Selecciona el criterio objetivo', ['BIDATING','por calidad de servicio en la zona', 'por calidad de la competencia', 'por interaccion comercial y consumo'])
extension = st.slider('Selecciona la extensión de la muestra',0,20,5,5)

# Realizar la predicción cuando se haga clic en el botón
if st.button('Recomendar'):
    df_recomendaciones = recomendacion(criterio, extension + 1)
    st.write('Recomendaciones de ciudades para Expansión según el criterio escogido:')
    st.dataframe(df_recomendaciones)
