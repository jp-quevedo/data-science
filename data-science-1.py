import pandas as pd
import numpy as np

data = './life-expectancy-data.csv'

df = pd.read_csv(data)
columns = df.columns

print(df.head()) # python3 entrega1.py