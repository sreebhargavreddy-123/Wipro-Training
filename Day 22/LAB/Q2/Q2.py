import pandas as pd
import numpy as np

# 1. Load CSV into DataFrame
df = pd.read_csv("sales.csv")

# 2. Add Total column
df["Total"] = df["Quantity"] * df["Price"]

# 3. NumPy calculations
total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
std_deviation = np.std(df["Total"])

print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation:", std_deviation)

# 4. Best-selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

print("Best Selling Product:", best_product)
