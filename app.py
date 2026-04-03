import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from national_parks import summarize_parks

df = pd.read_csv("data/processed/parks_final.csv")

st.title("National Parks Explorer")

st.markdown("""
### What does this mean?

This app compares National Park Service sites based on:
- **Amenities** (activities and campgrounds)
- **Operational complexity** (alerts)

Alerts represent things like closures, hazards, and maintenance issues. 
Parks with more infrastructure and visitors tend to have more alerts, 
so higher alert counts often reflect complexity rather than poor quality.

This helps explore how park features relate to real-world conditions.
""")

state_options = ["All"] + sorted(df["states"].dropna().unique().tolist())
selected_state = st.selectbox("Filter by State", state_options)

if selected_state == "All":
    df_filtered = df.copy()
else:
    df_filtered = df[df["states"].str.contains(selected_state, na=False)].copy()

st.subheader("Dataset Summary")
st.write(summarize_parks(df_filtered))

st.subheader("Top Parks")
sort_metric = st.selectbox(
    "Sort parks by:",
    ["num_alerts", "num_activities", "num_campgrounds"]
)
top_n = st.slider("Number of parks to show", 5, 20, 10)

st.dataframe(
    df_filtered.sort_values(sort_metric, ascending=False)
    .head(top_n)[["fullName", "states", "num_alerts", "num_campgrounds", "num_activities"]]
)

st.subheader("Full Dataset Preview")
st.dataframe(df_filtered.head(20))

st.subheader("Activities vs Alerts")
st.write("Is there a relationship between park amenities and operational complexity?")

plt.style.use("dark_background")
fig, ax = plt.subplots()

ax.scatter(df_filtered["num_activities"], df_filtered["num_alerts"], alpha=0.6)

if len(df_filtered) > 1:
    z = np.polyfit(df_filtered["num_activities"], df_filtered["num_alerts"], 1)
    p = np.poly1d(z)

    x_line = np.linspace(
        df_filtered["num_activities"].min(),
        df_filtered["num_activities"].max(),
        100
    )
    ax.plot(x_line, p(x_line))

ax.set_title("Activities vs Alerts")
ax.set_xlabel("Number of Activities")
ax.set_ylabel("Number of Alerts")
ax.grid(True, alpha=0.2)

st.pyplot(fig)

st.caption("Each point represents a park. Higher values indicate more activities and more active alerts.")

st.write("""
Most parks cluster between 0–3 alerts regardless of activity level, suggesting only a weak relationship between amenities and alerts. However, a few parks with higher activity counts also show elevated alert levels, indicating that larger or more complex parks may require more management.
""")