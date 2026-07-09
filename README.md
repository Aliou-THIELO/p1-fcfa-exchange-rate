# P1 — FCFA Exchange Rate Tracker

## Objective

This project tracks the evolution of the CFA franc (XOF) against non-euro currencies (USD, CNY), helping Senegalese SMEs, merchants, and individuals identify the right time to carry out international transactions (imports, trade exchanges).

## What this project does

The pipeline fetches daily exchange rates for USD → XOF, EUR → XOF, and CNY → XOF from an external API, validates the data structure, and stores it for further analysis (trends, alerts, visualization).

## Tech stack

- Python
- requests
- python-dotenv
- Pydantic *(coming soon)*
- Parquet *(coming soon)*

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

## Project structure

```
p1-fcfa-exchange-rate/
├── data/          # Raw and processed data
├── src/
│   └── ingest.py  # Exchange rate ingestion script
├── .env           # API key (not versioned)
├── requirements.txt
└── README.md
```