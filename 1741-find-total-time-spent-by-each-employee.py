import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_spent"] = employees["out_time"] - employees["in_time"]
    return (
        employees.groupby(["event_day", "emp_id"])["time_spent"]
        .sum()
        .reset_index(name="total_time")
        .rename(columns={"event_day": "day"})
    )
