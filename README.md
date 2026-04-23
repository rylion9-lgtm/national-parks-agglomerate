# National Parks: An Agglomerate

This project uses the National Park Service (NPS) API to build a curated dataset of U.S. National Park Service sites. The goal is to combine multiple API endpoints into a single, clean dataset that supports analysis and visualization.

---

## Project Website

View the full project site (documentation, tutorial, and report):  
https://rylion9-lgtm.github.io/national-parks-agglomerate/

---

## Live App

Explore the interactive Streamlit app here:  
https://national-parks-agglomerategit-fx4mzpepe8eaqgridzjnzr.streamlit.app/

---

## Project Goal

This project investigates how **park amenities** (activities and campgrounds) relate to **operational complexity** (alerts).

Rather than using a pre-existing dataset, this project builds one from scratch by:
- Collecting data from the NPS API
- Cleaning and transforming raw data
- Engineering useful features
- Merging multiple data sources into one dataset

---

## Data Sources

This project uses the official National Park Service API:
- Parks endpoint
- Alerts endpoint
- Campgrounds endpoint

To re-run the data collection process, you will need a free API key from:
https://www.nps.gov/subjects/developer/get-started.htm

Create a `.env` file in the root directory:
```
NPS_API_KEY=your_key_here
```

---

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/rylion9-lgtm/national-parks-agglomerate
cd national-parks-agglomerate
python -m pip install -e .
```

To run the Streamlit app, install Streamlit:

```bash
python -m pip install streamlit
```

---

## Running the App

```bash
streamlit run app.py
```

---

## Example Usage (Package)

```python
import pandas as pd
from national_parks import summarize_parks

df = pd.read_csv("data/processed/parks_final.csv")
summary = summarize_parks(df)

print(summary)
```

---

## Final Dataset

The final dataset is located at:

```
data/processed/parks_final.csv
```

It contains:
- 474 rows
- 9 columns

### Variables

- `fullName`: Full name of the park unit
- `parkCode`: Unique park identifier
- `states`: State abbreviation(s)
- `latitude`: Latitude
- `longitude`: Longitude
- `description_length`: Length of park description
- `num_activities`: Count of activities
- `num_alerts`: Number of alerts
- `num_campgrounds`: Number of campgrounds

---

## Key Insight

Most parks have relatively few alerts regardless of activity level, suggesting only a weak relationship between amenities and alerts. However, parks with more activities tend to show slightly higher alert counts, indicating increased operational complexity.

---

## Project Structure

```
national-parks-agglomerate/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── get_parks.py
│   ├── clean_parks.py
│   ├── get_alerts.py
│   ├── merge_alerts.py
│   ├── get_campgrounds.py
│   └── merge_campgrounds.py
│
└── national_parks/
    ├── __init__.py
    ├── data.py
    ├── clean.py
    └── analyze.py
```

---

## Notes and Limitations

- Data represents a snapshot in time (not live-updating)
- Alerts and campgrounds were limited to 500 records
- `num_activities` is an engineered approximation
- Park units vary widely in size and type

---

## Why This Project Matters

This project demonstrates:
- API data collection
- Data cleaning and transformation
- Feature engineering
- Multi-source data integration
- Building an installable Python package
- Deploying an interactive Streamlit app

It reflects a real-world data science workflow from raw data to deployed application.