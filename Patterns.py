# CRISTIANO WILSON

# This scripts aims to: 1-Data loading and inspection (read_excel, select_dtypes)
# 2-Data transformation (Label Encoding)
# 3-Preparation for ML (making all inputs numeric)
# 4-Saving results (to_excel)

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = "Dataset.xlsx"
df = pd.read_excel(file_path)

# Identify categorical columns
categorical_columns = df.select_dtypes(include=["object", "category"]).columns

# Apply Label Encoding to categorical columns
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# Save the encoded dataset
df.to_excel("Dataset.xlsx", index=False)
