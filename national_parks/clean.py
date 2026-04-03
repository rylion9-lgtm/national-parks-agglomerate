import pandas as pd

def clean_parks(df):
    df["description_length"] = df["description"].fillna("").apply(len)
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["num_activities"] = df["activities"].fillna("").apply(lambda x: x.count("name"))

    return df[[
        "fullName",
        "parkCode",
        "states",
        "latitude",
        "longitude",
        "description_length",
        "num_activities"
    ]]