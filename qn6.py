import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

restaurants_per_cuisine = df.groupby("cuisine")["restaurant_id"].nunique()

revenue_per_cuisine = df.groupby("cuisine")["total_amount"].sum()

cuisine_stats = pd.DataFrame({
    "num_restaurants": restaurants_per_cuisine,
    "total_revenue": revenue_per_cuisine
})

median_revenue = cuisine_stats["total_revenue"].median()
candidates = cuisine_stats[cuisine_stats["total_revenue"] >= median_revenue]

result_cuisine = candidates["num_restaurants"].idxmin()
result_stats = candidates.loc[result_cuisine]

print(f"Cuisine with lowest number of restaurants but still significant revenue: {result_cuisine}")
print(f"Number of restaurants: {result_stats['num_restaurants']}, Total revenue: {result_stats['total_revenue']}")

