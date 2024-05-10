import streamlit as st

st.header('st.checkbox')

st.write ('O que você gostaria de pedir?')

icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')

if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")

if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤")
