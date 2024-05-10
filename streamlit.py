import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# Função para gerar dados de vendas simuladas
def generate_sales_data():
    while True:
        # Simula dados de venda aleatórios
        product_id = random.randint(1, 100)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10.0, 100.0), 2)
        
        # Retorna os dados de venda simulados como um dicionário
        yield {"Product ID": product_id, "Quantity": quantity, "Price": price}
        
        # Aguarda um intervalo antes de gerar o próximo conjunto de dados
        time.sleep(1)

# Criar uma página da web com o Streamlit
def main():
    st.set_page_config(layout="wide")
    st.title("Dashboard de Vendas Simuladas")
    
    # Criar controles de filtro
    filter_options = st.sidebar.multiselect(
        "Selecione as colunas para visualizar",
        ["Product ID", "Quantity", "Price"]
    )
    
    # Criar uma lista vazia para armazenar os dados de vendas
    sales_data = []
    
    # Iniciar o streaming de dados de vendas simuladas
    for sale in generate_sales_data():
        # Adicionar a venda à lista de dados de vendas
        sales_data.append(sale)
        
        # Converter a lista de dados de vendas em um DataFrame
        sales_df = pd.DataFrame(sales_data)
        
        # Aplicar filtros selecionados
        if filter_options:
            sales_df = sales_df[filter_options]
        
        # Dividir a página em duas colunas
        col1, col2 = st.beta_columns(2)
        
        # Exibir gráfico de barras para quantidades vendidas de cada produto
        with col1:
            st.subheader("Quantidade Vendida de Cada Produto")
            product_counts = sales_df['Product ID'].value_counts()
            st.bar_chart(product_counts)
        
        # Exibir gráfico de linha para acompanhar a variação de preços ao longo do tempo
        with col2:
            st.subheader("Variação de Preços ao Longo do Tempo")
            sales_df['Timestamp'] = pd.Timestamp.now()
            sales_df['Timestamp'] = pd.to_datetime(sales_df['Timestamp'])
            price_data = sales_df[['Timestamp', 'Price']].set_index('Timestamp')
            st.line_chart(price_data)
        
        # Atualizar a tabela na página da web
        st.subheader("Tabela de Dados de Vendas")
        st.write(sales_df)
        
# Executar o aplicativo principal
if __name__ == "__main__":
    main()
