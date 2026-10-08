import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('Iris.csv')

print('==== Data Cleaning with numpy ====')
print('\n==== 1. Detect Missing Data ====')
# Detecting if there are any missing values in this dataset

missing_values = df.isnull().sum()

print('Missing Values per column: ')
print(missing_values)        # Check and calc for nulls per column
print(f'Total missing cells in the dataset is {missing_values.sum()}')

print('\n==== 2. Handling Missing Data ====')
# The Iris Dataset I'm using doesn't have missing data, so this dataset with missing values will help test out how we handle missing data with pandas.

sample_data = pd.DataFrame({
    'name': ['Mike', 'Dayo', 'Wisdom', 'Ademola'],
    'stud_age': [17, 19, np.nan, np.nan],
    'score': [85, 73, 89, np.nan]
})

print('Original Sample data is:\n', sample_data)    # Prints the original data

print('\nDrop rows where "stud_age" is missing: ')
print(sample_data.dropna(subset=['stud_age']))      # Drop missing values

# Fill missing scores with mean
mean_score = sample_data['score'].mean()
print(f'\nFill missing scores with mean ({mean_score:.1f}):')
print(sample_data['score'].fillna(mean_score))

print('\n==== 3. Finding & Removing Duplicates ====')

sample_data.loc[4] = ['Mike', 17, 85]   # Assigned duplicate by index
print('Data with a duplicate row:\n', sample_data)
print(f'Number of duplicate rows: {sample_data.duplicated().sum()}')

# Drop duplicates
print('\nAfter dropping duplicates: ')
print(sample_data.drop_duplicates())

print('\n==== 4. Selecting, Filtering & Sorting ====')
print('\n loc[0]: ')    # By index
print(df.loc[0])        # First row

print('\n iloc[0]: ')   # By position
print(df.iloc[0])       # First row but by position

# Boolean Filtering
# In the Iris dataset, let's find all Setosa flowers with a Sepal Length > 5.0
condition = (df['Species'] == 'Iris-setosa') & (df['SepalLengthCm'] > 5.0)
filtered_df = df[condition]
print(f'\nSetosa flowers with Sepal Length > 5.0 is: {len(filtered_df)} rows')
print(filtered_df.head())

# Finding items inside our Iris dataset
species_filter = df[df['Species'].isin(['Iris-versicolor', 'Iris-virginica'])]
print(f'\nVersicolor & Virginica rows: {len(species_filter)}')

# Sorting
print('\nTop 5 longest Sepal Lengths:')
print(df.sort_values('SepalLengthCm', ascending=False).head())