import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Upload de CSV')
uploaded_file = st.file_uploader("Escolha um arquivo")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Estatístiscas descritivas')
  st.write(df.describe())
else:
  st.info('☝️ Faça upload de um arquivo CSV')
