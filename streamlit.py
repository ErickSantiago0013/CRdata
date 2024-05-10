import time
import random

# Função para gerar dados de vendas simuladas
def generate_sales_data():
    while True:
        # Simula dados de venda aleatórios
        product_id = random.randint(1, 100)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10.0, 100.0), 2)
        
        # Imprime os dados de venda simulados
        print(f"Product ID: {product_id}, Quantity: {quantity}, Price: ${price}")
        
        # Aguarda um intervalo antes de gerar o próximo conjunto de dados
        time.sleep(1)

# Inicia a geração de dados de vendas simuladas
generate_sales_data()
