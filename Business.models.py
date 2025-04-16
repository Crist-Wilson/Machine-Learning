#Load dataset (replace 'dataset.xlsx' with your actual file)
df = pd.read_excel("Dataset.xlsx")

# Display basic information about the dataset
print(df.info())
print(df.head())

# Preprocessing (handling missing values, encoding categorical variables)
df.dropna(inplace=True)  # Remove missing values


