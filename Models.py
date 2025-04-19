import pandas as pd
#data = pd.read_excel("/Users/crist_wilson/Desktop/Allianz - Direct Debit-20250415/Dataset.xlsx")
#for Customer_ID  in data:
#print(Customer_ID)
#import pandas as pd

# Load the Excel file

# Load your dataset (ensure the correct file path)
data = pd.read_excel("/Users/crist_wilson/Desktop/Allianz - Direct Debit-20250415/Dataset.xlsx")

# Check if 'Customer_ID' exists in the DataFrame
if 'Customer_ID' in data.columns:
    for customer_id in data['Customer_ID']:
        print(customer_id)
else:
    print("Column 'Customer_ID' not found in the dataset.")
    