import pandas as pd

# -----------------------------
# Load the Dataset
# -----------------------------
df = pd.read_csv("titanic.csv")

print("Original Dataset Shape:", df.shape)

# -----------------------------
# Check Missing Values
# -----------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill missing Age values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove Cabin column because it has too many missing values
df.drop("Cabin", axis=1, inplace=True)

# -----------------------------
# Remove Duplicate Records
# -----------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# -----------------------------
# Remove Outliers (Age) using IQR
# -----------------------------
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[(df["Age"] >= lower_limit) & (df["Age"] <= upper_limit)]

# -----------------------------
# Display Results
# -----------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:", df.shape)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully as 'titanic_cleaned.csv'")