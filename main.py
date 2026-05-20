import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from utilitarios import outlier_calc, plot_params_and_show

# Carregando o arquivo
# Convertendo Postal Code para str para evitar erros com códigos começando com zero
df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding="latin_1",
    dtype={
        "Postal Code": str,
    },
)

# Visualização inicial dos dados
print("VISUALIZAÇÃO INICIAL DOS DADOS:")
print(df.head(), "\n")

# Visualização dos tipos de dados
print("VISUALIZAÇÃO DOS TIPOS DE DADOS:")
print(df.info(), "\n")

# Tratamento de duplicados
print("TRATAMENTO DE DUPLICADOS:")
duplicados = df.duplicated().sum()
print("Duplicados encontrados: ", duplicados)
print("Nenhum duplicado encontrado!", "\n")

# Tratamento de nulos
print("TRATAMENTO DE NULOS:")
nulos = df.isnull().sum().sum()
print("Nulos encontrados: ", nulos)
print("Nenhum nulo encontrado!", "\n")

# Identificação de valores inválidos
print("TRATAMENTO DE VALORES INVÁLIDOS:")

quantidade_invalida = len(df[df["Quantity"] <= 0])
print("Linhas com quantidade inválida: ", quantidade_invalida)

venda_invalida = len(df[df["Sales"] <= 0])
print("Linhas com venda inválida: ", venda_invalida)

print("Nenhum valor inválido encontrado!", "\n")

# Identificação de outliers
# Por meio de box plots
fig, axs = plt.subplots(nrows=2, ncols=2)

sns.boxplot(x=df["Sales"], ax=axs[0, 0])
axs[0, 0].set_title("Sales")

sns.boxplot(x=df["Quantity"], ax=axs[0, 1])
axs[0, 1].set_title("Quantity")

sns.boxplot(x=df["Discount"], ax=axs[1, 0])
axs[1, 0].set_title("Discount")

sns.boxplot(x=df["Profit"], ax=axs[1, 1])
axs[1, 1].set_title("Profit")

fig.suptitle("Identificação de outliers")

plt.show()

# Box Plot de Sales e Profit não são úteis, então gerando mais um gráfico sem eles
fig, axs = plt.subplots(ncols=2)

sns.boxplot(x=df["Quantity"], ax=axs[0])
axs[0].set_title("Quantity")

sns.boxplot(x=df["Discount"], ax=axs[1])
axs[1].set_title("Discount")

fig.suptitle("Identificação de outliers 2")

plt.show()

# Identificando outliers pelo método dos quantis
print("IDENTIFICANDO OUTLIERS")

outliers_quantity = outlier_calc(df, "Quantity")
outliers_discount = outlier_calc(df, "Discount")
outliers_sales = outlier_calc(df, "Sales")
outliers_profit = outlier_calc(df, "Profit")
print("\n")

# Como os outliers de sales e profit juntos são quase um terço do dataset, decidi não os remover
# Removendo apenas os outliers de Quantity e Discount
print("REMOVENDO OUTLIERS DE QUANTITY E DISCOUNT")
outliers_combinados = (
    pd.concat([outliers_quantity, outliers_discount])
    .drop_duplicates()
    .reset_index(drop=True)
)
print(outliers_combinados.head())

df_limpo = df[~df.isin(outliers_combinados)].dropna()
df_limpo[~df_limpo.isin(outliers_discount)].dropna(inplace=True)

print(f"{len(outliers_combinados)} outliers removidos")
print(
    f"Tamanho do novo dataframe: {len(df_limpo)}, {len(df_limpo) / len(df) * 100:.2f}% do dataset original"
)

# Salvando o df antigo para uma variável diferente
# e passando o limpo para df
df_antigo = df
df = df_limpo
print(len(df_antigo), len(df), "\n")

# Convertendo datas (formato mês/dia/ano)
# Criando novas colunas caso precise dos originais
# Prefixando todas as colunas criadas por mim com "MY" para ajudar na identificação
df["MY Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y", errors="coerce"
)
df["MY Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y", errors="coerce")

print("VISUALIZANDO NOVOS CAMPOS DE DATA:")
print(df.info(), "\n")

print("COMPARANDO DATAS:")
print(df[["Order Date", "MY Order Date"]])
print(df[["Ship Date", "MY Ship Date"]], "\n")

print(df["Sales"].sum())

# Feature Engineering
print("FEATURE ENGINEERING")

# Extraíndo apenas o mês e ano das datas, não acho que dia seja muito útil
df["MY Order Month"] = df["MY Order Date"].dt.month
print("EXTRAÍNDO MÊS DO PEDIDO")
print(df["MY Order Month"], "\n")

meses_map = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
df["MY Order Month Name"] = df["MY Order Month"].map(meses_map)

df["MY Order Year"] = df["MY Order Date"].dt.year
print("EXTRAÍNDO ANO DO PEDIDO")
print(df["MY Order Year"], "\n")

# Extraíndo tempo (dias) que o pedido levou para ser entregue
df["MY Days Taken"] = (df["MY Ship Date"] - df["MY Order Date"]).dt.days
print("EXTRAÍNDO TEMPO DE ENTREGA DO PEDIDO EM DIAS")
print(df["MY Days Taken"], "\n")

# AED
print("ANÁLISE EXPLORATÓRIA DE DADOS", "\n")

# Quais os países?
print(f"Países: {np.array2string(df['Country'].unique())}", "\n")

# Métricas de vendas
print(f"Total de vendas: {df['Sales'].sum():.2f}")
print(f"Venda média: {np.mean(df['Sales']):.2f}", "\n")

# Métricas de categorias
df_categorias = df.groupby("Category")

# Categorias com mais vendas
print("Número de vendas por categorias")
print(df_categorias.size().sort_values(ascending=False), "\n")

df_categorias.size().plot(kind="pie", autopct="%1.1f%%")
plot_params_and_show("Vendas por categoria", "", "", 90)

# Categorias com mais lucros
print("Lucro por categoria")
print(df_categorias["Profit"].sum().sort_values(ascending=False), "\n")

df_categorias["Profit"].sum().plot(kind="bar")
plot_params_and_show("Lucro por categoria", "Categoria", "Lucro", 0)

# Métricas de subcategorias
df_subcategorias = df.groupby("Sub-Category")

# Subcategorias com mais vendas
print("Número de vendas por subcategorias")
print(df_subcategorias.size().sort_values(ascending=False), "\n")

df_subcategorias.size().plot(kind="bar")
plot_params_and_show("Vendas por subcategoria", "Subcategoria", "Vendas", 45)

# Subcategorias com mais lucros
print("Lucro por subcategoria")
print(df_subcategorias["Profit"].sum().sort_values(ascending=False), "\n")

df_subcategorias["Profit"].sum().plot(kind="bar")
plot_params_and_show("Lucro por subcategoria", "Subcategoria", "Lucro", 45)

# Relação entre desconto e lucro?
df.plot(kind="scatter", x="Discount", y="Profit")
plot_params_and_show("Lucro por desconto", "Desconto", "Lucro", 45)

# Qual valor de desconto tem mais instâncias de lucro positivo?
df_desconto_positivo = df[df["Profit"] > 0].groupby("Discount")
df_desconto_positivo["Profit"].count().plot(kind="bar")
plot_params_and_show(
    "Instâncias de lucro positivo por desconto", "Nº de lucros", "Desconto", 45
)

# Informações sobre o tempo de entrega
print("INFORMAÇÕES SOBRE O TEMPO DE ENTREGA")
print(f"Mínimo: {df['MY Days Taken'].min()}")
print(f"Máximo: {df['MY Days Taken'].max()}")
print(f"Média: {df['MY Days Taken'].mean()}")

# Entregas no mesmo dia?
print(
    f"Quantidade de entregas no mesmo dia: {len(df[df['Order Date'] == df['Ship Date']])}",
    "\n",
)

# Top 10 Cidades
df_cidades = df.groupby("City")
df_cidades.size().nlargest(10).plot(kind="bar")
plot_params_and_show("Top 10 cidades com mais pedidos", "Cidades", "Pedidos", 45)

# New York City e Los Angeles tem liderança considerável
# Tempo de entrega médio para as duas primeiras cidades
df_cidades_ny_la = df[
    (df["City"] == "New York City") | (df["City"] == "Los Angeles")
].groupby("City")

print("TEMPO DE ENTREGA MÉDIO: TOP 2 CIDADES")
print(df_cidades_ny_la["MY Days Taken"].mean(), "\n")

# Cidades com mais entregas imediatas
df_cidades_entrega_imediata = df[df["MY Days Taken"] == 0].groupby("City")
df_cidades_entrega_imediata.size().nlargest(10).plot(kind="bar")
plot_params_and_show(
    "Top 10 cidades com mais entregas imediatas", "Cidades", "Entregas imediatas", 45
)

# Média de vendas por mês
df_meses = df.groupby("MY Order Month Name")
df_meses["Sales"].mean().plot(kind="line")
plt.xticks(range(1, 13), list(meses_map.values()))
plot_params_and_show("Média de pedidos por mês", "Mês", "Pedidos", 45)

# Crescimento de pedidos por ano
df_anos = df.groupby("MY Order Year")
df_anos["Sales"].size().plot(kind="line")
plot_params_and_show("Pedidos por ano", "Ano", "Pedidos", 45)
