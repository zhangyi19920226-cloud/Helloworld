import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Bob', None, 'David', 'Alice'],
    'age': [22, 25, 23, None, 22],
    'score': [88, 92, 79, 95, 88],
    'city': ['Beijing', 'Shanghai', 'Beijing', 'SHANGHAI', 'Beijing']
}
df = pd.DataFrame(data)
print(df)
print()
print(df.isnull())
print(df.isnull().sum())


