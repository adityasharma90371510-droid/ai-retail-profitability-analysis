import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
# ---- BUSINESS KPIs ---- #

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()

print("\n----- BUSINESS KPIs -----")
print("Total Revenue:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
# ---- PROFIT BY CATEGORY ---- #

profit_by_category = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\n----- PROFIT BY CATEGORY -----")
print(profit_by_category)
# ---- PROFIT BY SUB-CATEGORY ---- #

subcat_profit = df.groupby("Sub-Category")[["Sales","Profit"]].sum().sort_values(by="Profit")

print("\n----- PROFIT BY SUB-CATEGORY -----")
print(subcat_profit)
# ---- DISCOUNT IMPACT ANALYSIS ---- #

discount_analysis = df.groupby("Discount")[["Sales","Profit"]].mean()

print("\n----- DISCOUNT IMPACT -----")
print(discount_analysis)
# ---- EXPORT TABLES FOR DASHBOARD ---- #

profit_by_category.to_csv("outputs/profit_by_category.csv")
subcat_profit.to_csv("outputs/profit_by_subcategory.csv")
discount_analysis.to_csv("outputs/discount_analysis.csv")
print("\nTables exported successfully.")
    # ---- PROFIT BY REGION ---- #

region_profit = df.groupby("Region")[["Sales","Profit"]].sum()

print("\n----- PROFIT BY REGION -----")
print(region_profit)

region_profit.to_csv("outputs/profit_by_region.csv")