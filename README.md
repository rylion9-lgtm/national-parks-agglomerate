# National Parks: An Agglomerate

This project uses the National Park Service API to build a curated dataset of U.S. National Park Service sites. The goal was to create a park-level dataset that combines information from multiple API endpoints into one clean table for analysis.

## Live App

Explore the interactive Streamlit app here:  
https://national-parks-agglomerategit-fx4mzpepe8eaqgridzjnzr.streamlit.app/

---

## Project Goal

I wanted to build a dataset that could help compare park units across the National Park Service system using location, park descriptions, activities, alerts, and campground information.

More specifically, this project explores how **park amenities (activities, campgrounds)** relate to **operational complexity (alerts)** across park units.

---

## Data Sources

This project uses the official National Park Service API:

- Parks endpoint
- Alerts endpoint
- Campgrounds endpoint

The data was collected through the public API using Python. To re-run the data collection scripts, you will need a free API key from the [National Park Service Developer Portal](https://www.nps.gov/subjects/developer/get-started.htm). Store it in a `.env` file at the root of the project:
```
NPS_API_KEY=your_key_here
```
---

## Final Dataset

The final dataset is saved as:

`data/processed/parks_final.csv`

It contains **474 rows** and **9 columns**.

### Variables

- `fullName`: full name of the park unit
- `parkCode`: unique park code used by the NPS API
- `states`: state abbreviation(s) for the park unit
- `latitude`: latitude of the park unit
- `longitude`: longitude of the park unit
- `description_length`: number of characters in the park description
- `num_activities`: approximate count of activities listed for the park
- `num_alerts`: number of alerts associated with the park from the pulled alerts data
- `num_campgrounds`: number of campgrounds associated with the park from the pulled campgrounds data

---

## Key Insight

Most parks have relatively few alerts regardless of activity level, suggesting only a weak relationship between amenities and alerts. However, larger parks with more activities tend to show slightly higher alert counts, indicating increased operational complexity.

---

## Project Structure
```text
national-parks-agglomerate/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── app.py
├── test_package.py
│
├── data/
│   ├── raw/
│   │   ├── parks_raw.csv
│   │   ├── alerts_raw.csv
│   │   └── campgrounds_raw.csv
│   └── processed/
│       ├── parks_clean.csv
│       ├── parks_with_alerts.csv
│       └── parks_final.csv
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

- `src/` contains scripts used to build the dataset
- `national_parks/` contains the installable Python package
- `app.py` is the Streamlit app for interactive exploration

---

## Prerequisites

- Python 3.11+
- A [National Park Service API key](https://www.nps.gov/subjects/developer/get-started.htm) (only needed to re-run data collection)

---

## How to Run

1. **Clone the repository**
```bash
git clone https://github.com/rylion9-lgtm/national-parks-agglomerate
cd national-parks-agglomerate
```

2. **Install dependencies**
```bash
python -m pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run app.py
```

---

## Notes and Limitations

- The dataset represents a snapshot in time and does not automatically update
- Alerts and campgrounds were pulled with a limit of 500 records
- `num_activities` is an engineered approximation
- Park units vary widely in type and scale

---

## Why This Project Matters

This project demonstrates how to:

- Collect data from an API
- Clean and transform raw data
- Engineer meaningful features
- Combine multiple data sources
- Build an installable Python package
- Deploy an interactive application

Rather than using a pre-made dataset, this project builds one from scratch — reflecting a real-world data science workflow.