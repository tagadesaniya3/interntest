import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# Extract quarter (1, 2, 3, 4)
df["quarter"] = df["order_date"].dt.quarter

quarter_revenue = df.groupby("quarter")["total_amount"].sum()

top_quarter = quarter_revenue.idxmax()
top_revenue = quarter_revenue.max()

print(f"The quarter with highest total revenue is Q{top_quarter} with revenue {top_revenue}")