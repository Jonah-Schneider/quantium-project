import pandas as pd
import os

file1 = pd.read_csv("data/daily_sales_data_0.csv")
file2 = pd.read_csv("data/daily_sales_data_1.csv")
file3 = pd.read_csv("data/daily_sales_data_2.csv")
combined_file = pd.concat([file1, file2, file3])

pink_only_file = combined_file[combined_file["product"] == "pink morsel"]
pink_only_file["sales"] = pink_only_file["quantity"] * pink_only_file["price"]
final_file = pink_only_file[["sales", "date", "region"]]
final_file.to_csv("output.csv", index=False)

df_view = pd.read_csv('output.csv')
print(df_view)
