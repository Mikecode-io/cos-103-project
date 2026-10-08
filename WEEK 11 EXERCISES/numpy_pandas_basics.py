import pandas as pd
import numpy as np

# Numpy Array
studentMarks =  np.array([60, 78, 90, 85, 82])  # 79.0
print('You mean mark is: ', studentMarks.mean(), '\nYour highest mark is: ', studentMarks.max())
# Incrementing each marks by 10
print(studentMarks + 10)

# Pandas Series
ages  = pd.Series([18, 23, 17, 26, 20], name = 'age')

ages[0]     # 18
ages.mean() #


# Pandas Dataframe 

studentData =  {
    'name': ['Mike', 'Dayo', 'Wisdom', 'Ademola'],
    'stud_age': [17, 19, 18, 18]
}

df = pd.DataFrame(studentData)
df['stud_age']
df.loc[2]
print(df)
