import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))

st.write('Sua cor favorita é ', option)
