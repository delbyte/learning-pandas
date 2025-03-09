import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = list(pd.date_range(20250308, periods = 10))
covidcases = ["Covid-19", "Omicron", "Omega"]
df = pd.DataFrame(np.random.randn(10, 3), index = dates, columns = covidcases)

print(df)
print(df.head(1))
print(df.tail(1))
print(df.T)
print(df.describe())

print(df.sort_index(axis = 1, ascending=True))