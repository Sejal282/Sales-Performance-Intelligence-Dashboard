import pandas as pd
import numpy as np

df = pd.read_csv("../dataset/sales_data.csv")

df.drop_duplicates(inplace=True)

df.fillna(0, inplace=True)

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df['Month_Name'] = df['Order_Date'].dt.month_name()


df.to_csv("../dataset/cleaned_sales_data.csv", index=False)

print("Data Cleaning Completed Successfully")
