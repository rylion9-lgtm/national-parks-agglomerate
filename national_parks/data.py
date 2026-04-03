import os
from pathlib import Path
import requests
import pandas as pd
from dotenv import load_dotenv

def get_parks_data():
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path=env_path, override=True)

    API_KEY = os.getenv("NPS_API_KEY")

    url = "https://developer.nps.gov/api/v1/parks"
    params = {"api_key": API_KEY, "limit": 500}

    response = requests.get(url, params=params)
    response.raise_for_status()

    return pd.json_normalize(response.json()["data"])