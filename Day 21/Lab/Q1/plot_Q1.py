import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# -----------------------------
# 1️⃣ Line Chart using Matplotlib
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker='o', linestyle='-', color='blue')

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()


# -----------------------------
# 2️⃣ Bar Plot using Seaborn
# -----------------------------
# Create DataFrame for seaborn
data = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

plt.figure(figsize=(8, 5))

sns.barplot(x="Month", y="Sales", data=data)

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()
