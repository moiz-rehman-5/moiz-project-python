#P-3 sunday May 4 2026 11;06 AM
"""
E-commerce Order Analysis System
Scenario: You are working for an online store (like Amazon-lite).
Tasks:
•	Analyze orders dataset 
•	Find: 
o	monthly revenue trend 
o	top customers 
o	most returned products 
•	Create summary tables 
Skills:
•	groupby() advanced 
•	pivot_table 
•	time series grouping 
•	merging datasets 
"""
import pandas as pd 

ecommerce_orders = pd.read_csv(r"C:\Users\MOIZ\Desktop\ecommerce_orders.csv")
customer_profile =pd.read_csv(r"C:\Users\MOIZ\Desktop\customer_profiles.csv")

df_cmb = pd.merge(ecommerce_orders , customer_profile ,on="Customer_ID",)

df_cmb["Order_Date"] = pd.to_datetime(df_cmb["Order_Date"], format = "mixed")

df_cmb["year_month"] = df_cmb["Order_Date"].dt.to_period("M")
print()
print("\n--- 1. Monthly Revenue Trend (Delivered vs Returned) ---")

tran_pivot = pd.pivot_table(df_cmb,
                            values="Total_Price",
                            index = "year_month",
                            columns = 'Status',
                            aggfunc="sum",
                             fill_value = 0)
print(tran_pivot)
print()
print("\n--- 2. Top Customers by Revenue (Delivered Orders Only) ---")
deliverd_order =df_cmb[df_cmb["Status"] =="Delivered"]
print(deliverd_order)
print()
print("\n--- 3. Logistical Return Hotspots ---")
return_items = df_cmb[df_cmb["Status"] =="Returned"]
return_hotsopt = return_items.groupby("Product_Name" ).size().sort_values(ascending=False)
print(return_hotsopt)
df_cmb.to_csv("ecommerce_order_cleand.csv",index=False)

#----ended-----