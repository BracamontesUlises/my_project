import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir Histograma') #esto crea un botn

if hist_button: #si al hacer clic en el boton
    #escribe un mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    #crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #mostrat un grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir grafico de dispersion')

if scatter_button:
    #escribe un mensaje
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    #crea un grafico de dispersion
    fig = px.scatter(car_data, x="odometer")

    #muestra un grafico ploty interactivo
    st.plotly_chart(fig, use_container_width=True)