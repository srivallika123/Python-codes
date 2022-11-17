# Getting data from specific column

import pandas as pd

data = pd.read_csv(r'C:\Users\USER406\Desktop\Nov10\Giants.csv')
df = pd.DataFrame(data, columns=['CEO', 'Established'])
print(df)