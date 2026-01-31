import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

restaurant_stats = df.groupby("restaurant_id")["total_amount"].agg(["count", "mean"])

small_restaurants = restaurant_stats[restaurant_stats["count"] < 20]

top_restaurant = small_restaurants["mean"].idxmax()
top_avg = small_restaurants["mean"].max()

print(f"Restaurant with highest average order value but less than 20 orders: {top_restaurant} with average {top_avg}")