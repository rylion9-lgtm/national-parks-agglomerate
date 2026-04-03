import pandas as pd

def summarize_parks(df):
    return {
        "num_parks": len(df),
        "avg_activities": df["num_activities"].mean(),
        "avg_alerts": df["num_alerts"].mean(),
        "avg_campgrounds": df["num_campgrounds"].mean()
    }

def top_parks_by_alerts(df, n=5):
    return df.sort_values("num_alerts", ascending=False).head(n)