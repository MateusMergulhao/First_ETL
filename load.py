from pymongo import MongoClient

def load_data(df, connection_string):

    print("Carregando dados")

    client = MongoClient(connection_string)

    db = client["access_logs"]
    collection = db["user_logins"]

    data_dict = df.to_dict("records")

    collection.insert_many(data_dict)

    print("Dados inseridos")