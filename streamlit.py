import streamlit as st

st.title('st.form')

# Exemplo completo usando a notação with
st.header('1. Exemplo usando a notação `with`')
st.subheader('Cafeteira')

with st.form('my_form'):
    st.subheader('**Escolha seu café**')

    # Componentes de entrada
    coffee_bean_val = st.selectbox('Grão', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Torra', ['Clara', 'Média', 'Escura'])
    brewing_val = st.selectbox('Método', ['Aeropress', 'Filtrado', 'Prensa Francesa', 'Cafeteira Italiana', 'Globo'])
    serving_type_val = st.selectbox('Formato', ['Quente', 'Gelado', 'Frapê'])
    milk_val = st.select_slider('Leite', ['Não', 'Pouco', 'Médio', 'Muito'])
    owncup_val = st.checkbox('Trouxe o meu copo!')

    # Todo formulário deve ter um botão enviar
    submitted = st.form_submit_button('Enviar')

if submitted:
    st.markdown(f'''
        ☕ Você pediu:
        - Grão: `{coffee_bean_val}`
        - Torra: `{coffee_roast_val}`
        - Método: `{brewing_val}`
        - Formato: `{serving_type_val}`
        - Leite: `{milk_val}`
        - Trouxe o meu copo: `{owncup_val}`
        ''')
else:
    st.write('☝️ Faça o seu pedido!')


# Pequeno exemplo usando objeto
st.header('2. Exemplo com objeto')

form = st.form('my_form_2')
selected_val = form.slider('Escolha um valor')
form.form_submit_button('Enviar')

st.write('Valor escolhido: ', selected_val)
