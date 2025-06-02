
# CRISTIANO WILSON

# We are intending to: 1-Data cleaning and feature engineering (converting age bands) 
# 2-Encoding categorical variables for machine learning compatibility
# 3-Normalization to standardize input values
# 4-Unsupervised learning via K-Means clustering
# 5-Customer segmentation for targeted strategy or personalization

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import K

# Define age band mapping
age_band_mapping = {
    'B = 25-29': 27,
    'C = 30-39': 34,
    'D = 40-69': 55,
    'S = +69': 75
}

# Filter out rows with 'No age' and map age bands to numerical values
filtered_data = full_data[full_data['Customer_age'] != 'No age'].copy()
filtered_data['Customer_age'] = filtered_data['Customer_age'].map(age_band_mapping)

# Select relevant features
features = [
    'Customer_age', 'Customer_type', 'Customer_region', 'Product_type',
    'Annual_premium', 'Payment_frequency', 'Broker_region', 'Broker_cor'
]
data_for_clustering = filtered_data[features].copy()

# Encode categorical variables
categorical_features = ['Customer_type', 'Customer_region', 'Product_type', 'Payment_frequency', 'Broker_region']
for col in categorical_features:
    le = LabelEncoder()
    data_for_clustering[col] = le.fit_transform(data_for_clustering[col].astype(str))

# Handle missing values
data_for_clustering.fillna(0, inplace=True)

# Normalize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_clustering)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
clusters = kmeans.fit_predict(scaled_data)

# Append clusters to dataset
filtered_data['Customer_Segment_Cluster'] = clusters
