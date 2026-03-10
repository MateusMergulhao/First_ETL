import pandas as pd

def extract_data(file_path):
    print("Extraindo CSV")

    df = pd.read_csv(file_path) #adicionar aqui quando criar o arquivo 

    return df