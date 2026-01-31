import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

hyderabad_orders = df[df["city"] == "Hyderabad"]

total_revenue = round(hyderabad_orders["total_amount"].sum())

print(f"Total revenue from Hyderabad: Rs {total_revenue}")