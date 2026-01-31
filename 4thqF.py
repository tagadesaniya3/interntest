import pandas as pd
df = pd.read_csv("final_food_delivery_dataset.csv")

gold_orders = df[df["membership"] == "Gold"]

avg_order_value = round(gold_orders["total_amount"].mean(), 2)

print(f"Average order value for Gold members: Rs {avg_order_value}")