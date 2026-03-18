# National Parks: An Agglomerate

This project uses the National Park Service API to build a curated dataset of U.S. National Park Service sites. The goal was to create a park-level dataset that combines information from multiple API endpoints into one clean table for analysis.

## Project Goal

I wanted to build a dataset that could help compare park units across the National Park Service system using location, park descriptions, activities, alerts, and campground information.

## Data Sources

This project uses the official National Park Service API:

- Parks endpoint
- Alerts endpoint
- Campgrounds endpoint

The data was collected through the public API using Python.

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

## Project Structure

```text
national-parks-agglomerate/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── parks_raw.csv
│   │   ├── alerts_raw.csv
│   │   └── campgrounds_raw.csv
│   └── processed/
│       ├── parks_clean.csv
│       ├── parks_with_alerts.csv
│       └── parks_final.csv
└── src/
    ├── get_parks.py
    ├── clean_parks.py
    ├── get_alerts.py
    ├── merge_alerts.py
    ├── get_campgrounds.py
    └── merge_campgrounds.py