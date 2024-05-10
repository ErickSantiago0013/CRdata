import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('Sobre esta aplicação'):
  st.write("`st.experimental_get_query_params` recupera parâmetros da consulta(query paramaters) diretamente da URL do navegador.")

# 1. Instruções
st.header('1. Instruções')
st.markdown('''
Na barra de URL do seu navegador de internet, anexe o seguinte:
`?name=Jack&surname=Beanstalk`
depois da URL base `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
então ficará assim 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Conteúdos do st.experimental_get_query_params
st.header('2. Conteúdos do st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Recuperando e exibindo informações da URL
st.header('3. Recuperando e exibindo informações da URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Olá **{firstname} {surname}**, tudo bem?')
