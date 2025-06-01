
# CRISTIANO WILSON

# This code is developed to: 1-Data preprocessing with label encoding.
# 2-Train-test splitting to evaluate generalization.
# 3-Model training for both linear (Logistic Regression) and ensemble (Random Forest) methods.
# 4-Model evaluation using classification metrics.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
data = pd.read_excel("Dataset.xlsx")

# Encode categorical variables
categorical_cols = data.select_dtypes(include=['object']).columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Define features and target
X = data.drop("Is_direct_debit", axis=1)
y = data["Is_direct_debit"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

# Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Evaluation
log_accuracy = accuracy_score(y_test, y_pred_log)
rf_accuracy = accuracy_score(y_test, y_pred_rf)

log_report = classification_report(y_test, y_pred_log)
rf_report = classification_report(y_test, y_pred_rf)

print("Logistic Regression Accuracy:", log_accuracy)
print("Random Forest Accuracy:", rf_accuracy)
print("\nLogistic Regression Report:\n", log_report)
print("\nRandom Forest Report:\n", rf_report)
