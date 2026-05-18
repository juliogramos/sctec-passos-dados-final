import pandas as pd

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
print("TRATAMENTO DE DUPLICADOS")
duplicados = df.duplicated().sum()
print("Duplicados encontrados: ", duplicados)
print("Nenhum duplicado encontrado!", "\n")

# Tratamento de nulos
print("TRATAMENTO DE NULOS")
nulos = df.isnull().sum().sum()
print("Nulos encontrados: ", nulos)
print("Nenhum nulo encontrado!", "\n")

# Convertendo datas (formato mês/dia/ano)
# Criando novas colunas caso precise dos originais
# Prefixando todas as colunas criadas por mim com "MY" para ajudar na identificação
df["MY Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y", errors="coerce"
)
df["MY Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y", errors="coerce")

print("VISUALIZANDO NOVOS CAMPOS DE DATA")
print(df.info(), "\n")

print("COMPARANDO DATAS")
print(df[["Order Date", "MY Order Date"]])
print(df[["Ship Date", "MY Ship Date"]], "\n")
