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
    st.title("Dados de Vendas Simuladas")
    
    # Criar um dataframe vazio para armazenar os dados de vendas
    sales_df = pd.DataFrame(columns=["Product ID", "Quantity", "Price"])
    
    # Criar um componente para exibir o dataframe
    table = st.table(sales_df)
    
    # Iniciar o streaming de dados de vendas simuladas
    for sale in generate_sales_data():
        # Adicionar a venda ao dataframe
        sales_df = sales_df.append(sale, ignore_index=True)
        
        # Atualizar a exibição da tabela na página da web
        table.dataframe(sales_df)
        
# Executar o aplicativo principal
if __name__ == "__main__":
    main()
