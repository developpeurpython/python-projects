# -*- coding: utf-8 -*-
"""restaurant_recommendation_system.ipynb

Automatically generated by Colaboratory.

# **1. Import necessary libraries**
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""# **2. Load the dataset and display basic information**"""

# Load the dataset
data = pd.read_csv("TripAdvisor_RestaurantRecommendation.csv")
print(data.head())

# Print dataset information
print("Dataset Information:\n")
print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns: {data.shape[1]}")
print(f"\nColumns:\n{', '.join(data.columns)}")
print(f"\nData Types:\n{data.dtypes}\n")

# Print summary statistics
print("Summary Statistics:\n")
print(data.describe().to_string())

"""# **3. Preprocess the data**"""

# Select relevant columns
data = data[["Name", "Type"]]
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Drop rows with missing values
data = data.dropna()

"""# **4. Compute the similarity matrix and create a reverse mapping of restaurant names and DataFrame indices**"""

# Initialize the TfidfVectorizer and fit_transform the 'Type' column
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(data["Type"])

# Compute the cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Create a reverse mapping of restaurant names and DataFrame indices
indices = pd.Series(data.index, index=data['Name']).drop_duplicates()

"""# **5. Define the restaurant recommendation function and test the recommendation function**"""

# Define the restaurant recommendation function
def restaurant_recommendation(name, similarity=similarity, indices=indices):
    if name not in indices:
        print(f"The restaurant '{name}' is not found in the dataset. Please try again with a valid restaurant name.")
        return None
    index = indices[name]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11] # Exclude the restaurant itself
    restaurant_indices = [i[0] for i in similarity_scores]
    return data['Name'].iloc[restaurant_indices]

# Test the recommendation function
print("Recommended restaurants similar to 'Sixty Vines':\n", restaurant_recommendation("Sixty Vines"))