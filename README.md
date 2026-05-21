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

Após isso foi feita a identificação de outliers. As colunas de vendas, quantidade, desconto e lucro foram escolhidas para isso. Foi gerado um boxplot para cada coluna, mas apenas os boxplots de quantidade e desconto são visualmente úteis. Neles foi possível identificar claramente alguns outliers, que foram confirmados utilizando o método do IQR. Foid descoberto que os outliers de quantidade e desconto compõe aproximadamente 11% do dataset, e isso me pareceu uma quantidade aceitável de dados a serem removidos. Já os outliers de desconto e lucro compõe aproximadamente 1/3 do dataset, então não os removi.

As colunas de datas foram importadas como string. Converti essas colunas para objetos de data, mas salvei os resultados em novas colunas ao invés de sobrescrever os valores string. Decidi que usaria o prefixo "MY" para identificar fácilmente quais colunas foram criadas por mim.

Cogitei mudar o nome da coluna "Sales" para algo como "Renda", já que várias vezes me confundi quanto a pedidos e vendas, mas no fim decidi deixar como está. Então para deixar esclarecido: sempre que algum print ou gráfico se referir a "vendas", está na verdade se referindo à coluna "Sales" que é a renda recebida pelo pedido. Quando aparecer "compras" ou "pedidos", se trata ao número de pedidos, ou seja, o número de linhas em um certo grupo.

A partir dessas datas, fiz o feature engineering de dados que julguei serem interessantes: mês do pedido, ano do pedido e quantos dias o pedido levou para ser entregue.

### 4. Análise exploratória

Primeiramente decidi checar quais os países das compras, e descobri que o único país é Estados Unidos. Vi na página do dataset que existem mais de 500 valores únicos de cidade, então decidi não os investigar por enquanto.

Feito isso, investiguei as métricas básicas sobre vendas: o total em vendas registradas ($2049914.67) e a venda média ($228.28). Por curiosidade também chequei os 10 produtos mais vendidos, e identifiquei três produtos que tem uma liderança clara: envelopes grampeados, papel fácil de grampear e grampos.

Quanto às categorias, foi feito uma descoberta interessante: a categoria com mais vendas é a de suprimentos para escritório, mas a categoria que mais gera lucros é a de eletrônicos, que é a categoria com menos vendas.

Nas subcategorias, as duas que lideram as vendas são fichários e papel. As duas que lideram em lucros são copiadoras e celulares, o que condiz com a categoria de tecnologia ser a mais lucrativa. Duas subactegorias causam prejuízo: estantes de livros e mesas (muito prejuízo).

Após isso, analisei a relação entre desconto o lucro. O gráfico de pontos deixou aparente que as vendas com 0 e 20% de desconto tendem a gerar mais lucros. Um gráfico de barra filtrando apenas lucros positivos revelou que descontos acima de 40% não geram nenhum lucro. Uma descoberta surpreendente foi que a maioria das vendas foram realizadas com descontos de 0 e 20%, o que pode indicar que o fato desses valores gerarem mais lucro se deve apenas pela maior frequência e não por uma correlação real.

Checando os tempos de entrega, descobri que elas levam entre 0 e 7 dias, e que entregas imediatas compõe aproximadamente 5.5% de todas as entregas. Por curiosidade, resolvi analisar dados sobre as vendas por cidade para ver se o tempo de entrega tem alguma relação com as vendas. Nova Iorque é a cidade com mais vendas e com mais entregas imediatas, mas Los Angeles é a segunda em vendas e a quinta em entregas imediatas, então não há fortes evidências de uma correlação.

Finalmente, analisei as datas dos pedidos. Os meses que possuem a maior quantidade de pedidos são Novembro e Dezembro, o que condiz com os feriados de fim de ano como Natal e Ano Novo. Por curiosidade, verifiquei os produtos mais comprados em Novembro e Dezembro para ver se haviam alguns produtos mais "natalinos", mas o top 3 não se alterou.

Por fim, chequei o crescimento do número de pedidos e do lucro por ano. O número de pedidos parece estar aumentando exponencialmente, enquanto o lucro aumenta linearmente. Diria que essa loja está tendo bom crescimento financeiro.

## Principais Insights

- Tecnologia gera mais lucro mesmo não gerando tantas vendas
- Mesas geram muito prejuízo e não são tão vendidas, seria bom parar de vender elas
- Descontos acima de 40% não geram nenhum lucro
- Maior parte das vendas acontece Novembro e Dezembro, talves presentes?

## Dashboard
