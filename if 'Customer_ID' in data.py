if 'Customer_ID' in data.columns:
    for customer_id in data['Customer_ID']:
        print(customer_id)
else:
    print("Column 'Customer_ID' not found in the dataset.")
