import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# -----------------------------
# Load Cleaned Dataset
# -----------------------------
df = pd.read_csv("titanic_cleaned.csv")

# -----------------------------
# Identify Categorical Features
# -----------------------------
print("Categorical Features:")
categorical_columns = df.select_dtypes(include="object").columns
print(categorical_columns)

# -----------------------------
# Label Encoding
# -----------------------------
label_encoder = LabelEncoder()

df["Sex"] = label_encoder.fit_transform(df["Sex"])
df["Embarked"] = label_encoder.fit_transform(df["Embarked"])

print("\nLabel Encoding Applied to: Sex, Embarked")

# -----------------------------
# One-Hot Encoding
# -----------------------------
df = pd.get_dummies(df, columns=["Pclass"], drop_first=True)

print("One-Hot Encoding Applied to: Pclass")

# -----------------------------
# Standardization
# -----------------------------
scaler = StandardScaler()

df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])

print("\nStandardization Applied to: Age and Fare")

# -----------------------------
# Display Updated Dataset
# -----------------------------
print("\nFirst 5 Rows After Feature Engineering:")
print(df.head())

print("\nDataset Shape:", df.shape)

# -----------------------------
# Save Dataset
# -----------------------------
df.to_csv("titanic_feature_engineered.csv", index=False)

print("\nFeature engineered dataset saved successfully.")