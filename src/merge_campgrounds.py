import pandas as pd

print("Loading datasets...")

parks = pd.read_csv("data/processed/parks_with_alerts.csv")
campgrounds = pd.read_csv("data/raw/campgrounds_raw.csv")

print("Parks shape:", parks.shape)
print("Campgrounds shape:", campgrounds.shape)

if "parkCode" not in campgrounds.columns:
    raise ValueError("parkCode column not found in campgrounds data.")

campgrounds_count = (
    campgrounds.groupby("parkCode")
    .size()
    .reset_index(name="num_campgrounds")
)

final_df = parks.merge(campgrounds_count, on="parkCode", how="left")
final_df["num_campgrounds"] = final_df["num_campgrounds"].fillna(0).astype(int)

final_df.to_csv("data/processed/parks_final.csv", index=False)

print("Final dataset shape:", final_df.shape)
print(final_df.head())