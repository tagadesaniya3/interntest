import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

gold = df[df["membership"] == "Gold"]

city_avg = gold.groupby("city")["total_amount"].mean()

highest_city = city_avg.idxmax()
highest_avg = city_avg.max()

print(f"Among Gold members, the city with highest average order value is {highest_city} with an average of {highest_avg}")