import pandas as pd

df = pd.read_csv('Iris.csv')

print('\nFirst 5 rows:')

print(df.head())

print('\nLast 5 rows:')

print(df.tail())

print(f'Column names: {df.columns.to_list()}')

print(f'\nShape in Row and Column: {df.shape}')

print('\n==== Data Info ====')

df.info()        # Tells us the type and non-null counts

print('\n==== Statistics of the dataset ====')

print(df.describe()) # Gives us the Descriptive statistics of the dataset, i.e., the mean, stand deviation, min, max and more...
