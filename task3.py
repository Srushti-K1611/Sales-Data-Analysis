# Sales Data Analysis Project
# This script is designed to run without errors.
# It creates a sample CSV file automatically if one is not found.

import pandas as pd
import os

# -------------------------------
# Step 1: Ensure CSV file exists
# -------------------------------

file_name = "sales_data.csv"

# Create sample data if file does not exist
if not os.path.exists(file_name):
    sample_data = {
        "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
        "Quantity": [5, 10, 3, 2, 8],
        "Price": [50000, 15000, 20000, 50000, 15000]
    }
    sample_df = pd.DataFrame(sample_data)
    sample_df.to_csv(file_name, index=False)
    print("Sample sales_data.csv file created.\n")

# -------------------------------
# Step 2: Load the dataset
# -------------------------------

df = pd.read_csv(file_name)
print("Sales data loaded successfully.\n")

# -------------------------------
# Step 3: Explore the dataset
# -------------------------------

print("First five rows:")
print(df.head(), "\n")

print("Dataset information:")
df.info()
print()

print("Dataset shape:", df.shape, "\n")

# -------------------------------
# Step 4: Clean the data
# -------------------------------

# Handle missing values safely
if "Quantity" in df.columns:
    df["Quantity"] = df["Quantity"].fillna(0)

if "Price" in df.columns:
    df["Price"] = df["Price"].fillna(df["Price"].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Data cleaning completed.\n")

# -------------------------------
# Step 5: Analyze sales
# -------------------------------

# Ensure required columns exist
required_columns = {"Product", "Quantity", "Price"}
if not required_columns.issubset(df.columns):
    raise ValueError("Required columns are missing from the dataset.")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Metrics
total_revenue = df["Revenue"].sum()
total_quantity_sold = df["Quantity"].sum()
average_price = df["Price"].mean()

product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

# -------------------------------
# Step 6: Generate report
# -------------------------------

print("Sales Analysis Report")
print("---------------------")
print("Total revenue:", round(total_revenue, 2))
print("Total quantity sold:", int(total_quantity_sold))
print("Best-selling product:", best_selling_product)
print("Units sold (best product):", int(best_selling_quantity))
print("Average product price:", round(average_price, 2))

print("\nProgram executed successfully.")

