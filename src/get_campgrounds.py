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

url = "https://developer.nps.gov/api/v1/campgrounds"
params = {
    "api_key": API_KEY,
    "limit": 500
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
campgrounds = data["data"]

df = pd.json_normalize(campgrounds)
df.to_csv("data/raw/campgrounds_raw.csv", index=False)

print("Saved campgrounds data:", df.shape)

cols_to_show = [col for col in ["parkCode", "name"] if col in df.columns]
if cols_to_show:
    print(df[cols_to_show].head())
else:
    print(df.head())