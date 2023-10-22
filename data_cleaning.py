# Data Cleaning:

# 1. Verify the computation of 'Total Sales'
uploaded_df["Computed Total Sales"] = uploaded_df["Quantity"] * uploaded_df["Price"]
incorrect_total_sales_rows = uploaded_df[uploaded_df["Total Sales"] != uploaded_df["Computed Total Sales"]]

# 2. Check for potential outliers in 'Quantity', 'Price', and 'Total Sales'
quantiles = uploaded_df[["Quantity", "Price", "Total Sales"]].quantile([0.01, 0.99])

# Feature Engineering:

# Extract year, month, and day from the 'Date' column
uploaded_df["Year"] = uploaded_df["Date"].dt.year
uploaded_df["Month"] = uploaded_df["Date"].dt.month
uploaded_df["Day"] = uploaded_df["Date"].dt.day

incorrect_total_sales_rows, quantiles
