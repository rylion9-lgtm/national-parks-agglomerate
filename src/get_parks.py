import os
from pathlib import Path

import requests
import pandas as pd
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
print("Looking for .env at:", env_path)
print("Exists:", env_path.exists())

load_dotenv(dotenv_path=env_path, override=True)

API_KEY = os.getenv("NPS_API_KEY")
print("API key found:", API_KEY is not None)

if not API_KEY:
    raise ValueError("NPS_API_KEY was not found in your .env file.")

url = "https://developer.nps.gov/api/v1/parks"
params = {
    "api_key": API_KEY,
    "limit": 500
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
parks = data["data"]

df = pd.json_normalize(parks)
df.to_csv("data/raw/parks_raw.csv", index=False)

print("Saved parks data:", df.shape)
print(df[["fullName", "parkCode", "states"]].head())