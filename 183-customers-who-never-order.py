import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(
        orders,
        how="left",
        left_on="id",
        right_on="customerId"
    )
    
    result = merged[merged["customerId"].isna()][["name"]]
    result.columns = ["Customers"]
    
    return result
