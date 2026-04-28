import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../dataset/sales_data.csv")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Create Month Name column
df['Month_Name'] = df['Order_Date'].dt.month_name()

# Save cleaned dataset
df.to_csv("../dataset/cleaned_sales_data.csv", index=False)

print("Data Cleaning Completed Successfully")