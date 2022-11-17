# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses

import pandas as pd

# Intialise data of lists
data = {'Name':['Tom', 'nick', 'Krish', 'Jack'], 'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

print(df)
