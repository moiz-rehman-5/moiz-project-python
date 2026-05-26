#P-2  sunday May 4 2026 9:46 AM
"""
Sales Report Cleaner
Scenario: Company gives messy sales data.
Tasks:
•	Fix missing product names 
•	Convert date formats 
•	Add new column: total = quantity * price 
•	Find: 
o	best-selling product 
o	daily revenue 
Skills:
•	datetime in pandas 
•	column operations 
•	aggregation 

"""""
import pandas as pd 

data = pd .read_csv(r"C:\Users\MOIZ\Desktop\messy_sales_data.csv")

df = pd.DataFrame(data)
print("-----raw data-----")
print(df.head(10))
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ' , "_")

df = df.fillna({
    'product_name':"unknown_product",
    "quantity":0,
    "price_per_unit": 0
     }
)
df['date'] = pd.to_datetime(df['date'], format="mixed")
df = df.sort_values(by="date")

df["total_revenue"] = (
    df["quantity"].fillna(0) * df["price_per_unit"].fillna(0)
)
print()
print("-----final result of clean data-----")
print(df.head(10))
print()
print("\n--- Top Products by Total Quantity Sold ---")
bussiness_report = df.groupby("product_name")["quantity"].sum()
print()
print("--- Daily Revenue ---")
daily_revenue = df.groupby("date")["total_revenue"].sum()

df.to_csv("Cleaned_sales_data.csv", index=False)

#----ended------
