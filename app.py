import pandas as pd
import streamlit as st

from national_parks import summarize_parks, top_parks_by_alerts

df = pd.read_csv("data/processed/parks_final.csv")

st.title("National Parks Explorer")

st.subheader("Dataset Summary")
st.write(summarize_parks(df))

st.subheader("Top Parks by Alerts")
st.dataframe(top_parks_by_alerts(df)[["fullName", "num_alerts", "num_campgrounds", "num_activities"]])

st.subheader("Full Dataset Preview")
st.dataframe(df.head(20))