import pandas as pd
from national_parks import summarize_parks, top_parks_by_alerts

df = pd.read_csv("data/processed/parks_final.csv")

print(summarize_parks(df))
print(top_parks_by_alerts(df)[["fullName", "num_alerts"]])