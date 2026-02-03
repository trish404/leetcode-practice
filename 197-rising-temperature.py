import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.copy()
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])

    prev = weather.rename(
        columns={
            "id": "prev_id",
            "recordDate": "prev_date",
            "temperature": "prev_temp",
        }
    )

    merged = weather.merge(
        prev,
        left_on="recordDate",
        right_on=prev["prev_date"] + pd.Timedelta(days=1),
        how="inner",
    )

    ans = merged.loc[merged["temperature"] > merged["prev_temp"], ["id"]]
    return ans.rename(columns={"id": "Id"})
