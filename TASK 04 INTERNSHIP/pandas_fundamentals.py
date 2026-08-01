import pandas as pd

# -------------------------------
# 1. Create Series and DataFrames
# -------------------------------

series = pd.Series([85, 90, 78, 92], index=["Ali", "Ahmed", "Sara", "Ayesha"])
print("Series:")
print(series)

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 21, 19, 22],
    "Department": ["CS", "SE", "CS", "IT"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# -------------------------------------------
# 2. Indexing, Filtering, Sorting & Selection
# -------------------------------------------

print("\nFirst Two Rows:")
print(df.head(2))

print("\nSelect Name and Marks:")
print(df[["Name", "Marks"]])

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# -------------------------
# 3. GroupBy Operation
# -------------------------

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

# -------------------------
# 4. Merge and Join
# -------------------------

fees = pd.DataFrame({
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Fee_Status": ["Paid", "Paid", "Unpaid", "Paid"]
})

merged_df = pd.merge(df, fees, on="Name")

print("\nMerged DataFrame:")
print(merged_df)

joined_df = df.join(fees["Fee_Status"])

print("\nJoined DataFrame:")
print(joined_df)