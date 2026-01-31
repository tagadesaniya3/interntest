import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

gold = df[df["membership"] == "Gold"]

result = gold.groupby("city")["total_amount"].sum().idxmax()

print(result)