import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = list(pd.date_range("20250308", periods = 10))
covidcases = ["Covid-19", "Omicron", "Omega"]
df = pd.DataFrame(np.random.randn(10, 3), index = dates, columns = covidcases)

print(f"the numbers for Omicron are \n{df['Omicron']}")

print(f"The first three rows of data-\n{df[0:3]}")

print(f"Querying data from specific dates-\n{df['20250310':'20250317']}")