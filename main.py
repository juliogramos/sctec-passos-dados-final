import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

# Valores de Sales e Profit não são úteis, então gerando mais um gráfico sem eles
fig, axs = plt.subplots(ncols=2)

sns.boxplot(x=df["Quantity"], ax=axs[0])
axs[0].set_title("Quantity")

sns.boxplot(x=df["Discount"], ax=axs[1])
axs[1].set_title("Discount")

fig.suptitle("Identificação de outliers 2")

plt.show()

# TBD - QUANTILES
