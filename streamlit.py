import streamlit as st

st.title('🖼️ yt-img-app')
st.header('Gerador de miniaturas (thumbnails) (thumbnails) de vídeos do YouTube')

with st.expander('Sobre'):
  st.write('Esta aplicação extrai miniaturas (thumbnails) de um vídeo do Youtube.')

# Configuração da imagem
st.sidebar.header('Configurações')
img_dict = {'Máxima': 'maxresdefault', 'Alta': 'hqdefault', 'Média': 'mqdefault', 'Padrão': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Selecione a qualidade da miniatura', ['Máxima', 'Alta', 'Média', 'Padrão'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Cole a URL do YouTube', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# Exibe a imagem da miniatura
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('URL da miniatura (thumbnail) do vídeo do YouTube: ', yt_img)
else:
  st.write('☝️ Insira uma URL para continuar ...')
