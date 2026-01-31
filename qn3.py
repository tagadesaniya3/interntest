import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

user_total = df.groupby("user_id")["total_amount"].sum()

high_spenders = user_total[user_total > 1000]

num_users = high_spenders.shape[0]

print(f"Number of distinct users who spent more than Rs 1000: {num_users}")