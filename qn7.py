import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

total_orders = df.shape[0]

gold_orders = df[df["membership"] == "Gold"].shape[0]

percentage = round((gold_orders / total_orders) * 100)

print(f"Percentage of orders placed by Gold members: {percentage}%")