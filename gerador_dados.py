import json
import random
import csv
from datetime import datetime, timedelta

# Lê o arquivo JSON com a lista de produtos
with open('produtos.json') as f:
    produtos = json.load(f)

# Define as datas para gerar as compras
data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2023, 3, 31)

# Gera a base de CSV
with open('compras.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Nome do Produto', 'Marca', 'Preço', 'Custo', 'Data da Venda', 'Data da Compra', 'Categoria', 'Peso'])
    for i in range(1000):
        # Seleciona um produto aleatório
        produto = random.choice(produtos)
        marca = random.choice(produto['marcas'])
        preco = round(random.uniform(produto['menor_preco'], produto['maior_preco']), 2)
        custo = round(preco * random.uniform(0.7, 0.9), 2)
        data_venda = data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days))
        data_compra = data_venda - timedelta(days=random.randint(0, 30))
        categoria = produto['categoria']
        peso = produto['peso']
        # Escreve a linha no CSV
        writer.writerow([produto['produto'], marca, preco, custo, data_venda.strftime('%d/%m/%Y'), data_compra.strftime('%d/%m/%Y'), categoria, peso])
