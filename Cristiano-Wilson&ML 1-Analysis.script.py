
# CRISTIANO WILSON

# Our objective is to: 1-DataFrame manipulation with pandas
# 2-Data cleaning (renaming, converting data types)
# 3-Feature engineering (age binning)
# 4-Exploratory Data Analysis (EDA) using group by and mean()
# 5-Exporting results with pd.ExcelWriter

import pandas as pd

# Load datasets
file_paths = [
    "Dataset.xlsx"
]
df_list = [pd.read_excel(path) for path in file_paths]
df = pd.concat(df_list, ignore_index=True)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Rename target variable for clarity
df.rename(columns={'is_direct_debit': 'direct_debit_used'}, inplace=True)

# Convert age to numeric and group
df['customer_age'] = pd.to_numeric(df['customer_age'], errors='coerce')
df['age_group'] = pd.cut(df['customer_age'], bins=[0, 25, 40, 60, 100], labels=['<25', '26-40', '41-60', '60+'])

# Compute group-wise direct debit usage
age_pattern = df.groupby('age_group')['direct_debit_used'].mean().reset_index()
region_pattern = df.groupby('customer_region')['direct_debit_used'].mean().reset_index()
broker_pattern = df.groupby('broker_account_number')['direct_debit_used'].mean().reset_index().sort_values(by='direct_debit_used', ascending=False).head(10)
contract_pattern = df.groupby('product_type')['direct_debit_used'].mean().reset_index()

# Save all patterns to Excel
with pd.ExcelWriter("/mnt/data/DirectDebit_Usage_Patterns.xlsx") as writer:
    age_pattern.to_excel(writer, sheet_name="By_Age_Group", index=False)
    region_pattern.to_excel(writer, sheet_name="By_Region", index=False)
    broker_pattern.to_excel(writer, sheet_name="Top_Brokers", index=False)
    contract_pattern.to_excel(writer, sheet_name="By_Product_Type", index=False)

    
