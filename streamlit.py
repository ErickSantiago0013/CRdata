import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Exemplo 1

st.subheader('Slider')

age = st.slider('Quantos anos você tem?', 0, 130, 25)
st.write("Eu tenho ", age, ' anos')




age = st.slider('teste', 1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10)
st.write("o teste deu", age, 'de idade')

# Exemplo 2

st.subheader('Slider de intervalo')

values = st.slider(
     'Escolha um intervalo de valores',
     0.0, 100.0, (25.0, 75.0))
st.write('Valores:', values)

# Exemplo 3

st.subheader('Slider de intervalo de tempo')

appointment = st.slider(
     "Agende um compromisso:",
     value=(time(11, 30), time(12, 45)))
st.write("O compromisso foi agendado para:", appointment)

# Exemplo 4

st.subheader('Slider de data e hora')

start_time = st.slider(
     "Quando você vai começar?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Início:", start_time)
