import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

# Define rating bins (example: 0-1, 1-2, ..., 4-5)
bins = [3.0 , 3.5, 4.0 , 4.5 , 5]
labels = ["3.0-3.5", "3.6-4.0" ,"4.1-4.5" , "4.6-5.0"]

# Create a new column for rating range
df["rating_range"] = pd.cut(df["rating"], bins=bins, labels=labels, right=False)

# Group by rating_range and sum total_amount
rating_revenue = df.groupby("rating_range")["total_amount"].sum()

# Find the rating range with the highest total revenue
highest_range = rating_revenue.idxmax()
highest_revenue = rating_revenue.max()

print(f"The restaurant rating range generating highest total revenue is {highest_range} with revenue {highest_revenue}")