import pandas as pd
import json
import sqlite3

orders = pd.read_csv("orders.csv")

with open("users.json", "r") as f:
    users_data = json.load(f)

users = pd.DataFrame(users_data)

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

with open("restaurants.sql", "r") as f:
    cursor.executescript(f.read())

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

merged1 = orders.merge(users, on="user_id", how="left")

final_df = merged1.merge(restaurants, on="restaurant_id", how="left")

final_df.to_csv("final_food_delivery_dataset.csv", index=False)

print(" Final dataset created successfully!")


