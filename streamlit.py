import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.write('Você selecionou:', options)
