import pandas as pd
data = pd.read_excel("/Users/crist_wilson/Desktop/Allianz - Direct Debit-20250415/Dataset.xlsx")
for Customer_ID  in data:
     print(Customer_ID)
