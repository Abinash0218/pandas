# Sales Data Analysis

import pandas as pd

data={
    "Order_id": [101, 102, 103, 104, 105],
    "Products": ["Laptop", "Laptop", "Tab", "Mobile", "Ipad"],
    "Region": ["N", "E", "N", "W", "SE"],
    "Sales": [8, 6, 3, 7, 8],
    "Quantity": [2, 3, 1, 2, 1],
    "Date": ["2026-01-23", "2026-02-03", "2026-03-23", "2026-02-03", "2026-03-23"]
}
print(data)

df=pd.DataFrame(data)
print(df)

df["Date"]=pd.to_datetime(df["Date"]) # to convert the string to date

high_sales=df[df["Sales"]>=8]
print(high_sales)

region_sales=df.groupby("Region", sort=False)["Sales"].sum()
print("========Regionwise_Sales========")
print(region_sales)

product_analysis=df.groupby("Products").agg({
    "Sales":"sum",
    "Quantity":"mean"
})
print("========product_analysis========")
print(product_analysis)

# Sorting of Data
sorted_data=df.sort_values("Sales",ascending=False)
print("========Sorted_Data========")
print(sorted_data)

# Time based analysis
monthly_sales=df.groupby(df["Date"].dt.month)["Sales"].sum()
print("========Monthly_Sales========")
print(monthly_sales)

# pivot table
pivot=pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Products",
    aggfunc="sum"
)
print("========Pivot Table========")
print(pivot)