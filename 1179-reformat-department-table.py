import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun",
                   "Jul","Aug","Sep","Oct","Nov","Dec"]

    return (
        department.pivot(
            index="id",
            columns="month",
            values="revenue"
        )
        .reindex(columns=months)
        .rename(columns=lambda x: f"{x}_Revenue")
        .reset_index()
    )
