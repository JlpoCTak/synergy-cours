import pandas as pd
import numpy as np

s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])

# print(s)
# print()
# print(s['a'])
# print()
# print(s[['a', 'b']])
# print()
# print(s[1:])
# print()
# print(s+s)

data = {'Name': ['Alice', 'Sofia', 'Igor'],
        'Age': [25, 34, 56],
        'City': ['Min Vody', 'Moscow', 'Omsk']}

df = pd.DataFrame(data)
# print(df)

data1 = [['Alice', 25, 'Moscow'],
         ['Maria', 45, 'Vologda'],
         ['Vlad', 23, 'Omsk']]
df1 = pd.DataFrame(data1, columns=['Name', "Age", 'City'])
print(df1)
df.to_csv('dz9_data.csv', index=False, sep=',', encoding='utf-8')
print()
print(df1.head(3))
print()
print(df1.tail(3))

