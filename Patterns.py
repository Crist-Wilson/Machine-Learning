# Count how many customers use direct debit
direct_debit_customers = data[data['Payment_Method'] == 'Direct Debit']['Customer_ID'].nunique()

# Analyze brokers with the most direct debit contracts
broker_analysis = data[data['Payment_Method'] == 'Direct Debit'].groupby('Broker_Name')['Contract_ID'].count()

import pandas as pd

# Load your data
data = pd.read_excel("/path/to/Dataset.xlsx")

# Filter only Direct Debit payments
direct_debit_data = data[data['Payment_Method'] == 'Direct Debit']

# Group by location and count instances
locations_summary = direct_debit_data.groupby('Location')['Customer_ID'].count()

# Sort in descending order to see the highest usage
most_direct_debit_locations = locations_summary.sort_values(ascending=False)

print(most_direct_debit_locations)
