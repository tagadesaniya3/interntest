import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

combo_revenue = df.groupby(["city", "cuisine"])["total_amount"].sum()

top_combo = combo_revenue.idxmax()
top_revenue = combo_revenue.max()

print(f"Combination contributing highest revenue: {top_combo} with revenue {top_revenue}")