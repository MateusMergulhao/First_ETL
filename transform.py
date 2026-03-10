def transform_data(df):
    print("Transformando os dados")

    #remover valores nulos
    df = df.dropna()

    #remover duplicados
    df = df.drop_duplicates()

    return df