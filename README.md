# Desafio Extra - Superstore

Desafio extra do curso "Introdução ao Data Science" do programa [SCTEC](https://sctec.scti.sc.gov.br/).

Elaborado por [Julio Gonçalves Ramos](https://www.linkedin.com/in/julio-ramos-1684a5390/).

Link para o repositório: [https://github.com/juliogramos/sctec-passos-dados-final](https://github.com/juliogramos/sctec-passos-dados-final)

Link para o Notebook: [https://colab.research.google.com/drive/1cDIKwTC0Z5_I8z-CbBbn90IeDoWr0f5r?usp=sharing](https://colab.research.google.com/drive/1cDIKwTC0Z5_I8z-CbBbn90IeDoWr0f5r?usp=sharing)

## Tecnologias

- Python
- Pandas
- Numpy
- Matplotlib

## Como visualizar localmente

### Executar Notebook

1. Acessar o notebook: [link](https://colab.research.google.com/drive/1cDIKwTC0Z5_I8z-CbBbn90IeDoWr0f5r?usp=sharing)
2. Executar células em ordem OU usar o botão Run All
   Não é preciso baixar o dataset manualmente, ele é baixado através da biblioteca do Kagglehub e salvo em cache.

### Executar arquivo Python

1. Clonar o repositório ou baixar os arquivos e extrair em uma pasta
2. Baixar o dataset: [link](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
3. Colocar o arquivo CSV na mesma pasta que o arquivo main.py e utilitarios.py
4. Instalar o Python (versão utilizada: 3.12.3) e o Pip
5. Instalar a biblioteca virtualenv com o comando: pip3 install virtualenv
6. Criar um novo ambiente virtual com o comando: virtualenv venv
7. Ativar o ambiente virtual com o comando (Mac e Linux): source venv/bin/activate
8. Instalar as bibliotecas com o comando: pip install -r requirements.txt
9. Rodar o arquivo com o comando: python main.py

## Etapas de desenvolvimento

### 1. Definição do formato

O projeto foi primeiro desenvolvido em um arquivo Python, para que o código possa ser guardado no Github mais facilmente. Após todo o código ser escrito, um notebook foi criado a partir desse código para mais fácil compartilhamento e visualização do projeto.

### 2. Importação e compreensão dos dados

Para deixar a importação dos arquivos ainda mais conveniente, o notebook utiliza a biblioteca do Kagglehub para baixar o dataset para cache. Para a versão em código, o arquivo CSV do dataset deve ser baixado manualmente e colocado na mesma pasta que o arquivo main.py. O CSV não está incluído no repositório github, mas será enviado na entrega do projeto pelo AVA.

Um arquivo com duas funções utilitárias criadas ao longo do desenvolvimento do projeto também foi produzido. Essas funções estão presentes em uma célula separada na versão notebook.

Após a importação, foram executados os métodos head e info para a checagem inicial do dataset. O campo "Postal Code" originalmente é implementado como int, mas decidi converter ele para string durante a importação. Isso é uma boa prática que foi ensinada nas Trilhas Rápidas de dados: caso o código postal começar com o número zero, esse número será ocultado durante a conversão para inteiro do Python, e o código deixará de ser válido. As demais colunas possuem tipos adequados e não foram modificadas.

### 3. Tratamento e preparação dos dados

Primeiramente realizei a checagem de valores duplicados, e não existia nenhum. O comando info já havia mostrado que não havia valores nulos no dataset mas resolvi fazer a checagem mesmo assim. Também foram verificados valores inválidos, como quantidade negativa de produtos e venda com valor nulo ou negativo, e nenhum foi encontrado.

## Principais Insights

## Dashboard
