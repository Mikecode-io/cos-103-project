import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')
df = df.drop('Id', axis=1)

print('==== Grouping and Merging Dataset using Pandas ====')
print('\n==== 1. Creating New Columns =====')

# Vectorized Math
# Creating a 'PetalArea' column: length * width
df['PetalArea'] = df['PetalLengthCm'] * df['PetalWidthCm']
print(df[['PetalLengthCm', 'PetalWidthCm', 'PetalArea']].head())
print('\n')

print('==== 2. Making a New Column ====')
# Let's label flowers as 'Small' if PetalLength < 3.0, else 'Large'
# I'm using apply() here because it's an if/else check, not plain math
df['Size'] = df['PetalLengthCm'].apply(lambda x: 'Small' if x < 3.0 else 'Large')
print(df[['PetalLengthCm', 'Size']].head(10))   # Show the PetalLength and the new Size column
print('\n')

print('==== 3. GroupBy: Split-Apply-Combine ====')

print('Average Sepal Length per Species:')
print(df.groupby('Species')['SepalLengthCm'].mean())
print('\n')

print('==== 4. Merging ====')
garden_locations = pd.DataFrame({
    'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    'Garden': ['North Field', 'South Field', 'Greenhouse']
})

print('Our tiny "Garden" table:')
print(garden_locations)
print()

# Now merge the main df with garden_locations
# We join them on the 'Species' column, which exists in BOTH tables
merged_df = pd.merge(df, garden_locations, on='Species')

print('Merged table:')  # Show the first 5 rows
print(merged_df[['Species', 'Garden', 'PetalLengthCm']].head())
