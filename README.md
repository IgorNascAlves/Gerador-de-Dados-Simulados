# Gerador de Dados Simulados
Este projeto consiste em gerar dados simulados de compras de produtos de mercado e eletrônicos, a partir de um arquivo JSON com informações de 200 produtos. O objetivo é simular compras aleatórias e gerar um arquivo CSV com informações sobre essas compras, incluindo nome do produto, marca, preço, custo, data da venda, data da compra, categoria e peso.

Esse projeto foi desenvolvido em Python 3 e utiliza as bibliotecas pandas e matplotlib para manipulação de dados e geração de gráficos. Ele foi co-produzido com o ChatGPT, um modelo de linguagem natural desenvolvido pela OpenAI.

# Como usar
1 - Clone o repositório em sua máquina:

```
git clone https://github.com/seu-usuario/gerador-dados-simulados.git
```

2 - Instale as dependências do projeto:

```
pip install pandas matplotlib
```

3 - Execute o arquivo gerador_dados.py para gerar o arquivo CSV com os dados simulados de compras:

```
python gerador_dados.py
```

4 - Os dados gerados serão salvos no arquivo **'compras.csv'**.


# Estrutura do arquivo JSON
O arquivo **'produtos.json'** contém um objeto JSON com uma lista de 200 produtos. Cada produto é representado por um objeto JSON com as seguintes propriedades:

"Nome do Produto": string com o nome do produto
"Marca": lista de strings com as marcas do produto
"Maior Preço": número decimal com o preço máximo do produto
"Menor Preço": número decimal com o preço mínimo do produto
"Categoria": string com a categoria do produto (ex: alimentos, limpeza, eletrônicos, etc)
"Peso": string com a unidade de medida e o peso do produto (ex: "kg 1.5", "g 500")

# Autoria
Este projeto foi desenvolvido por Igor do Nascimento Alves, formado em Ciência da Computação, em colaboração com o ChatGPT, um modelo de linguagem natural desenvolvido pela OpenAI.
