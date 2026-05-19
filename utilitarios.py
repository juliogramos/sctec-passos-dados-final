from pandas import DataFrame


def outlier_calc(df: DataFrame, coluna: str):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    print(
        f"Outliers em {coluna}: {len(outliers)}, {len(outliers) / len(df) * 100:.2f}% do dataset"
    )
    return outliers
