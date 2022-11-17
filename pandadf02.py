import pandas as pd

data = {'Country': ['Belgiun', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
        'Population': [11118900, 983283721, 2145322333]}
df = pd.DataFrame(data, columns = ['Country', 'Capital', 'Population'])
print(df)
