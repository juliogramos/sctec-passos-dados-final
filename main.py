import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from utilitarios import outlier_calc

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

# Feature Engineering
print("FEATURE ENGINEERING")

# Extraíndo apenas o mês das datas, não acho que dia e ano sejam muito úteis
df["MY Order_Month"] = df["MY Order Date"].dt.month
print("EXTRAÍNDO MÊS DO PEDIDO")
print(df["MY Order_Month"], "\n")

# Extraíndo tempo (dias) que o pedido levou para ser entregue
df["MY Days Taken"] = (df["MY Ship Date"] - df["MY Order Date"]).dt.days
print("EXTRAÍNDO TEMPO DE ENTREGA DO PEDIDO EM DIAS")
print(df["MY Days Taken"], "\n")
