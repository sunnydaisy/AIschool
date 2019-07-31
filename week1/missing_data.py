import pandas as pd
import numpy as np

df = pd.read_csv('./data/train.csv')
print('Before removing Missing Data')
df.info()

def remove_NAN(df):
    index_remove = []
    for key in df.keys():
        for i, data in enumerate(df[key]):
            if pd.isnull(data):
                index_remove.append(i)
    index_remove = list(set(index_remove))

    removed_data = df.drop(index = index_remove)
    return removed_data

removed_df = remove_NAN(df)
print('After removing Missing Data')
removed_df.info()    