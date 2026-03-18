import pandas as pd

print("Loading datasets...")

parks = pd.read_csv("data/processed/parks_clean.csv")
alerts = pd.read_csv("data/raw/alerts_raw.csv")

print("Parks shape:", parks.shape)
print("Alerts shape:", alerts.shape)

if "parkCode" not in alerts.columns:
    raise ValueError("parkCode column not found in alerts data.")

alerts_count = (
    alerts.groupby("parkCode")
    .size()
    .reset_index(name="num_alerts")
)

final_df = parks.merge(alerts_count, on="parkCode", how="left")
final_df["num_alerts"] = final_df["num_alerts"].fillna(0).astype(int)

final_df.to_csv("data/processed/parks_with_alerts.csv", index=False)

print("Final dataset shape:", final_df.shape)
print(final_df.head())