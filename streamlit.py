import streamlit as st
import requests

st.title('🏀 Bored API')

st.sidebar.header('Entrada')
selected_type = st.sidebar.selectbox('Escolha um tipo de atividade', ["educação", "recreação", "social", "faça você mesmo", "caridade", "cozinhar", "relaxar", "música", "tarefas pequenas"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('Sobre'):
    st.write('Você está com tédio? A **Bored API** fornece sugestões de atividades que você pode fazer quando estiver com tédio. Esta aplicação é alimentado pela API Bored.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

st.header('Atividade sugerida')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Número de Participantes', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Tipo da atividade', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Preço', value=suggested_activity['price'], delta='')
