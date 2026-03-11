import pandas as pd

def transform_data(df):
    print("Transformando os dados")

    #remover valores nulos
    df = df.dropna()

    #remover duplicados
    df = df.drop_duplicates()

    # converter datetime
    df["datetime"] = pd.to_datetime(df["datetime"])

    return df