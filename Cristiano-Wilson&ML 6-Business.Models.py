#Load dataset (replace 'dataset.xlsx' with your actual file)
df = pd.read_excel("Dataset.xlsx") 

# Display basic information about the dataset
print(df.info())
print(df.head())

# Preprocessing (handling missing values, encoding categorical variables)
df.dropna(inplace=True)  # Remove missing values


# Splitting the dataset
X = df.drop("Status", axis=1)  # Replace "Status" with target column
y = df["Status"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training and evaluating models
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier()
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    print(f"{name} Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print(classification_report(y_test, y_pred))

# Plot feature importance for Random Forest
rf = models["Random Forest"]
importances = rf.feature_importances_
feature_names = X.columns
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance")
plt.show()
