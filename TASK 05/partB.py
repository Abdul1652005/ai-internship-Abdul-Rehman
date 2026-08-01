import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("titanic_cleaned.csv")

# Set plot style
sns.set_style("whitegrid")

# -----------------------------------
# 1. Histogram - Age Distribution
# -----------------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.savefig("histogram.png")
plt.show()

# -----------------------------------
# 2. Boxplot - Fare
# -----------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(y=df["Fare"])
plt.title("Boxplot of Fare")
plt.savefig("boxplot.png")
plt.show()

# -----------------------------------
# 3. Correlation Heatmap
# -----------------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# -----------------------------------
# 4. Survival Count Plot
# -----------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.savefig("survival_count.png")
plt.show()

# -----------------------------------
# 5. Passenger Class vs Survival
# -----------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Passenger Class vs Survival")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.savefig("class_survival.png")
plt.show()

print("\nAll graphs created successfully!")