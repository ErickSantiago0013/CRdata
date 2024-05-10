import streamlit as st

st.set_page_config(layout="wide")

st.title('Como customizar o Layout de uma aplicação Streamlit')

with st.expander('Sobre esta aplicação'):
  st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Entrada')
user_name = st.sidebar.text_input('Qual o seu nome?')
user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])

st.header('Saída')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Olá {user_name}!')
  else:
    st.write('👈  Por favor escreva seu **nome**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} é o seu **emoji** favorito!')
  else:
    st.write('👈 Por favor escolha um **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
  else:
    st.write('👈 Por favor escolha sua **comida** favorita!')
