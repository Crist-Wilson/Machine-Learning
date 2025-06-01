
# CRISTIANO WILSON 

# We seek to demonstrate: 1-Merges datasets across files
# 2-Cleans and encodes categorical data
# 3-Trains a Random Forest model
# 4-Extracts and visualizes feature importance
# 5-Helps Allianz understand which variables most influence direct debit adoption

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Step 1: Load and combine all Excel chunks
file_paths = [
    "Dataset.xlsx"
]
df_list = [pd.read_excel(fp) for fp in file_paths]
data = pd.concat(df_list, ignore_index=True)

# Step 2: Drop non-predictive columns (e.g., IDs)
columns_to_drop = ['Contract_number', 'Customer_ID', 'Broker_account_number', 'Customer_age']
data = data.drop(columns=columns_to_drop)

# Step 3: Encode categorical variables
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].fillna("Missing")  # Handle missing values
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

# Step 4: Split features and target
X = data.drop(columns=['Is_direct_debit'])
y = data['Is_direct_debit']

# Step 5: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Extract feature importances
Importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Step 8: Plot feature importances
plt.figure(figsize=(10, 6))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.gca().invert_yaxis()
plt.title('Feature Importances for Direct Debit Prediction')
plt.xlabel('Relative Importance')
plt.tight_layout()
plt.savefig("Allianz_Feature_Importance.png")
plt.show()
