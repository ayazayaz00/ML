import pandas as pd
import numpy as np

data = {
    'student_id': range(101, 121),
    'internal_marks1': [78, 85, np.nan, 67, 74, 92, 88, np.nan, 100, 65, 70, 95, 83, 77, np.nan, 60, 82, 90, 110, 68],
    'internal_marks2': [82, 88, 90, np.nan, 76, 96, 85, 75, 99, np.nan, 72, 91, 87, np.nan, 68, 64, 89, 92, 105, 70],
    'external_marks': [80, 87, 95, 65, np.nan, 100, 93, 88, 105, 60, 75, np.nan, 85, 78, 92, 58, 90, 98, 120, np.nan],
    'attendance': [90, 95, 85, 80, 88, 100, 92, 75, 98, 70, 80, 97, 89, 83, 76, 65, 85, 93, 100, 78],
    'age': [18, 19, 18, 20, 19, 21, 20, 22, 19, 18, 20, 21, 19, 22, 20, 21, 18, 19, 23, 20]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA:\n")
print(df)

columns_with_missing = ['internal_marks1', 'internal_marks2', 'external_marks']

for col in columns_with_missing:

    total = 0
    count = 0

    for value in df[col]:
        if not pd.isna(value):
            total += value
            count += 1

    mean = total / count

    for i in range(len(df)):
        if pd.isna(df.at[i, col]):
            df.at[i, col] = mean

print("\nDATA AFTER REPLACING MISSING VALUES:\n")
print(df)

numerical_cols = ['internal_marks1', 'internal_marks2', 'external_marks', 'attendance', 'age']
df[numerical_cols] = df[numerical_cols].astype(float)

for col in numerical_cols:

    min_val = df[col][0]
    max_val = df[col][0]

    for value in df[col]:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    for i in range(len(df)):
        df.at[i, col] = (df.at[i, col] - min_val) / (max_val - min_val)

print("\nDATA AFTER MIN-MAX NORMALIZATION:\n")
print(df)
