import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

gold_orders = df[df["membership"] == "Gold"].shape[0]

print(f"Total orders placed by Gold members: {gold_orders}")