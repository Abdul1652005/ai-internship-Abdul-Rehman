import pandas as pd

# Read dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Survival count
print("\nSurvival Count:")
print(df["Survived"].value_counts())

# Average age of passengers
print("\nAverage Age:")
print(df["Age"].mean())

# Average fare by passenger class
print("\nAverage Fare by Passenger Class:")
print(df.groupby("Pclass")["Fare"].mean())

# Survival by gender
print("\nSurvival by Gender:")
print(df.groupby("Sex")["Survived"].mean())

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as cleaned_titanic.csv")