import numpy as np
from datetime import date
import pandas as pd

df = pd.read_excel("data/raw/superstore.xlsx")

sales_df = df[["Order ID","Order Date", "Ship Date","Ship Mode","Customer ID","Product ID","Sales","Quantity","Discount","Profit",]]

print("\nSales Dataset Preview\n")
print(sales_df.head())
print("Rows:", sales_df.shape[0])
print("Columns:", sales_df.shape[1])

customers_df = (
    df[["Customer ID", "Customer Name","Segment","City", "State", "Postal Code", "Region", "Country"  ]]
    .drop_duplicates(subset=["Customer ID"],keep="first")
    .copy()
)

print("\nCustomer Dataset")
print(customers_df.head())
print(f"\nRows: {customers_df.shape[0]}")
print(f"Columns: {customers_df.shape[1]}")

#AS WE DONT HAVE INVENTORY INFO, WE WILL CREATE A NEW DATASET WITH PRODUCT ID AND SOME RANDOM INVENTORY DATA
products_df = (
    df[[ "Product ID", "Product Name", "Category", "Sub-Category" ]].drop_duplicates().copy()
)

inventory_df = products_df[["Product ID"]].copy()
inventory_df["Stock Quantity"] = np.random.randint(10,500,size=len(inventory_df))
inventory_df["Reorder Level"] = np.random.randint(10,50,size=len(inventory_df))
inventory_df["Last Updated"] = date.today()

print("\nProduct Dataset")
print(products_df.head())
print(f"\nRows: {products_df.shape[0]}")
print(f"Columns: {products_df.shape[1]}")

print("\nInventory Dataset")
print(inventory_df.head())
print(f"\nRows: {inventory_df.shape[0]}")
print(f"Columns: {inventory_df.shape[1]}")

sales_df.to_csv(
    "data/processed/sales.csv",
    index=False
)
customers_df.to_csv(
    "data/processed/customers.csv",
    index=False
)
products_df.to_csv(
    "data/processed/products.csv",
    index=False
)
inventory_df.to_csv(
    "data/processed/inventory.csv",
    index=False
)

print("\nCSV files created successfully.")