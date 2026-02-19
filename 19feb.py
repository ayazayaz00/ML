import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    'student_id': range(101, 121),
    'internal_marks1': [78, 85, np.nan, 67, 74, 92, 88, np.nan, 100, 65, 70, 95, 83, 77, np.nan, 60, 82, 90, 110, 68],
    'internal_marks2': [82, 88, 90, np.nan, 76, 96, 85, 75, 99, np.nan, 72, 91, 87, np.nan, 68, 64, 89, 92, 105, 70],
    'external_marks': [80, 87, 95, 65, np.nan, 100, 93, 88, 105, 60, 75, np.nan, 85, 78, 92, 58, 90, 98, 120, np.nan],
    'attendance': [90, 95, 85, 80, 88, 100, 92, 75, 98, 70, 80, 97, 89, 83, 76, 65, 85, 93, 100, 78],
    'age': [18, 19, 18, 20, 19, 21, 20, 22, 19, 18, 20, 21, 19, 22, 20, 21, 18, 19, 23, 20]
}

df = pd.DataFrame(data)
print("Original DataFrame with missing values:\n", df)

df.fillna(df.mean(), inplace=True)
print("\nDataFrame after replacing missing values with mean:\n", df)

scaler = MinMaxScaler()
numerical_cols = ['internal_marks1', 'internal_marks2', 'external_marks', 'attendance', 'age']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("\nDataFrame after Min-Max Normalization:\n", df)
