import streamlit as st
import plotly_express as px
import pandas as pd

st.header('Datos de anuncios de venta de coches')
car_data = pd.read_csv('c:/Users/cary_/OneDrive/Escritorio/Data analyst/Sprint 5/Proyecto5/my_proyect_sprint5/vehicles_us.csv') # leer los datos
st.write('Selecciona histograma o gráfico de dispersión')
build_histogram = st.button('Construir un histograma')
build_scatter = st.button('Construir gráfico de dispersion')


if build_histogram:
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if build_scatter:
    st.write('Creación de gráfico de dispersión el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

