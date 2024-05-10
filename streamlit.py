import streamlit as st
import time

st.title('st.progress')

with st.expander('Sobre esta aplicação'):
     st.write('Agora você pode exibir o progresso od seus calculosthe progress of your e, uma aplicação Streamlit com o comando `st.progress`.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
