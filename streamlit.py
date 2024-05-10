import streamlit as st
import pandas as pd
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
    st.title("Dashboard de Vendas Simuladas")
    
    # Criar controles de filtro
    filter_options = st.sidebar.multiselect(
        "Selecione as colunas para visualizar",
        ["Product ID", "Quantity", "Price"]
    )
    
    # Criar uma lista vazia para armazenar os dados de vendas
    sales_data = []
    
    # Criar um componente para exibir a tabela na página da web
    table = st.table(pd.DataFrame())
    
    # Iniciar o streaming de dados de vendas simuladas
    for sale in generate_sales_data():
        # Adicionar a venda à lista de dados de vendas
        sales_data.append(sale)
        
        # Converter a lista de dados de vendas em um DataFrame
        sales_df = pd.DataFrame(sales_data)
        
        # Aplicar filtros selecionados
        if filter_options:
            sales_df = sales_df[filter_options]
        
        # Atualizar a tabela na página da web
        table.dataframe(sales_df)
        
# Executar o aplicativo principal
if __name__ == "__main__":
    main()
