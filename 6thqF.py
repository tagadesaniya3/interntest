import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

gold = df[df["membership"] == "Gold"]

top_city = gold.groupby("city")["total_amount"].sum().idxmax()

num_orders = gold[gold["city"] == top_city].shape[0]

print(f"Number of orders in the top revenue city ({top_city}) among Gold members: {num_orders}")