import os
from pathlib import Path

import requests
import pandas as pd
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path, override=True)

API_KEY = os.getenv("NPS_API_KEY")

if not API_KEY:
    raise ValueError("NPS_API_KEY was not found in your .env file.")

url = "https://developer.nps.gov/api/v1/alerts"
params = {
    "api_key": API_KEY,
    "limit": 500
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
alerts = data["data"]

df = pd.json_normalize(alerts)
df.to_csv("data/raw/alerts_raw.csv", index=False)

print("Saved alerts data:", df.shape)

if "parkCode" in df.columns:
    print(df[["parkCode", "title"]].head())
else:
    print(df.head())