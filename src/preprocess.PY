import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_data(path):
    return pd.read_csv(path)


def clean_data(df):
    df = df.sort_values(["machine_id", "timestamp"])
    


def normalize(df, columns):
    # columns = ["temperature", "vibration",
    #            "humidity", "pressure", "energy_consumption"]

    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
