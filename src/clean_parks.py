import pandas as pd

df = pd.read_csv("data/raw/parks_raw.csv")

df["description_length"] = df["description"].fillna("").apply(len)

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

df["num_activities"] = df["activities"].fillna("").apply(lambda x: x.count("name"))

df_clean = df[[
    "fullName",
    "parkCode",
    "states",
    "latitude",
    "longitude",
    "description_length",
    "num_activities"
]]

df_clean.to_csv("data/processed/parks_clean.csv", index=False)

print("Clean dataset shape:", df_clean.shape)
print(df_clean.head())