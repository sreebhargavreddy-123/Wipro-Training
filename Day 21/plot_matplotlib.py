import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

names = ["A", "B", "C"]
scores = [80, 90, 100]

marks = [50, 60, 80, 70, 77, 86]

labels = ["Chrome", "Firefox", "Edge"]
sizes = [60, 25, 15]

# Create subplot layout
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# 1️⃣ Basic Line Plot
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 0].set_title("Simple Line", fontsize=10)

# 2️⃣ Styled Line Plot
axs[0, 1].plot(x, y, marker='o', linestyle='--')
axs[0, 1].set_title("Styled Line", fontsize=10)
axs[0, 1].set_xlabel("X Axis", fontsize=8)
axs[0, 1].set_ylabel("Y Axis", fontsize=8)
axs[0, 1].grid(True)

# 3️⃣ Bar Chart
axs[1, 0].bar(names, scores)
axs[1, 0].set_title("Student Scores", fontsize=10)

# 4️⃣ Scatter Plot
axs[1, 1].scatter(x, y)
axs[1, 1].set_title("Scatter Plot", fontsize=10)

# 5️⃣ Histogram
axs[2, 0].hist(marks, bins=5)
axs[2, 0].set_title("Marks Distribution", fontsize=10)

# 6️⃣ Pie Chart
axs[2, 1].pie(sizes, labels=labels, autopct='%1.1f%%',
              textprops={'fontsize': 8})
axs[2, 1].set_title("Browser Usage", fontsize=10)

# Adjust spacing
plt.subplots_adjust(hspace=0.5, wspace=0.4)

plt.show()