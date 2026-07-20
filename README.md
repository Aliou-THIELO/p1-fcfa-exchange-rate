# P1 — FCFA Exchange Rate Tracker

## Objective

This project tracks the evolution of the CFA franc (XOF) against non-euro currencies (USD, CNY), helping Senegalese SMEs, merchants, and individuals identify the right time to carry out international transactions (imports, trade exchanges).

## What this project does

The pipeline fetches daily exchange rates for USD → XOF, EUR → XOF, and CNY → XOF from an external API, validates the data structure using Pydantic, and stores the result as a daily Parquet file for further analysis (trends, alerts, visualization).

## Tech stack

- Python
- requests
- python-dotenv
- Pydantic
- pandas
- Parquet

## Installation

1. Clone the repo
```bash
   git clone https://github.com/Aliou-THIELO/p1-fcfa-exchange-rate.git
   cd p1-fcfa-exchange-rate
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file at the project root with your API key:

```
   API_token=your_api_key_here
```
## Data

Data files are not tracked in version control, except for one sample file (`data/2026-07-20.parquet`) demonstrating the pipeline's output format. Each run generates a new Parquet file partitioned by date.

## Project structure

```
p1-fcfa-exchange-rate/
├── data/ # Daily exchange rate snapshots (Parquet, mostly untracked)
├── src/
│ ├── ingest.py # API client, validation, and Parquet export
│ └── schemas.py # Pydantic models for API response validation
├── .env # API key (not versioned)
├── requirements.txt
└── README.md
```