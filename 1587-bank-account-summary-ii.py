import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    totals = (
        transactions
        .groupby("account")["amount"]
        .sum()
        .reset_index(name="balance")
    )
    return (
        users.merge(
            totals, on="account", how="inner"
        ).query("balance > 10000")
        [["name", "balance"]]
    )
