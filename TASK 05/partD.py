import sqlite3
import pandas as pd

# -----------------------------
# Load the Cleaned Dataset
# -----------------------------
df = pd.read_csv("titanic_cleaned.csv")

# -----------------------------
# Create SQLite Database
# -----------------------------
conn = sqlite3.connect("titanic.db")

# Store dataset in SQL table
df.to_sql("passengers", conn, if_exists="replace", index=False)

print("Database 'titanic.db' created successfully!")

# -----------------------------
# SELECT Query
# -----------------------------
print("\n========== SELECT QUERY ==========")

query1 = pd.read_sql("""
SELECT Name, Age, Fare
FROM passengers
LIMIT 5;
""", conn)

print(query1)

# -----------------------------
# WHERE Query
# -----------------------------
print("\n========== WHERE QUERY ==========")

query2 = pd.read_sql("""
SELECT Name, Fare
FROM passengers
WHERE Fare > 50;
""", conn)

print(query2)

# -----------------------------
# GROUP BY Query
# -----------------------------
print("\n========== GROUP BY QUERY ==========")

query3 = pd.read_sql("""
SELECT Survived,
COUNT(*) AS TotalPassengers
FROM passengers
GROUP BY Survived;
""", conn)

print(query3)

# -----------------------------
# Create Second Table for JOIN
# -----------------------------
class_df = pd.DataFrame({
    "Pclass": [1, 2, 3],
    "ClassName": ["First Class", "Second Class", "Third Class"]
})

class_df.to_sql("classes", conn, if_exists="replace", index=False)

# -----------------------------
# JOIN Query
# -----------------------------
print("\n========== JOIN QUERY ==========")

query4 = pd.read_sql("""
SELECT
p.Name,
c.ClassName,
p.Survived
FROM passengers p
JOIN classes c
ON p.Pclass = c.Pclass
LIMIT 10;
""", conn)

print(query4)

# -----------------------------
# Close Database
# -----------------------------
conn.close()

print("\nAll SQL queries executed successfully!")