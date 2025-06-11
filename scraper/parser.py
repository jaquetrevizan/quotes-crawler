import pandas as pd

def display_with_pandas(path_csv="output/quotes.csv"):
    df = pd.read_csv(path_csv)
    print(df.head())
