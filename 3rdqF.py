import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

num_users = df["user_id"].nunique()

print(f"Number of distinct users who placed at least one order: {num_users}")