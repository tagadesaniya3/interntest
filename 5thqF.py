import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

high_rating_orders = df[df["rating"] >= 4.5]

num_orders = high_rating_orders.shape[0]

print(f"Number of orders for restaurants with rating >= 4.5: {num_orders}")