import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

cuisine_avg = df.groupby("cuisine")["total_amount"].mean()

highest_cuisine = cuisine_avg.idxmax()
highest_avg = cuisine_avg.max()

print(f"The cuisine with the highest average order value is {highest_cuisine} with an average of {highest_avg}")