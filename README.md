# P1 — FCFA Exchange Rate Tracker

## Objectif

Ce projet vise à suivre l'évolution du franc CFA (XOF) face aux devises hors zone euro (USD, CNY), afin d'aider les PME, commerçants et particuliers sénégalais à identifier le bon moment pour effectuer leurs transactions internationales (importations, échanges commerciaux).

##  Ce que fait ce projet

Le pipeline récupère quotidiennement les taux de change USD → XOF, EUR → XOF et CNY → XOF depuis une API externe, valide la structure des données, puis les stocke pour une analyse ultérieure (tendances, alertes, visualisation).

##  Stack technique

- Python
- requests
- python-dotenv
- Pydantic *(à venir)*
- Parquet *(à venir)*

##  Installation

1. Cloner le repo
```bash
   git clone https://github.com/Aliou-THIELO/p1-fcfa-exchange-rate.git
   cd p1-fcfa-exchange-rate
```
2. Installer les dépendances
```bash
   pip install -r requirements.txt
```
3. Créer un fichier `.env` à la racine avec ta clé API :

```
   API_token=ta_cle_ici
```

## Structure du projet

```
p1-fcfa-exchange-rate/
├── data/          # Données brutes et transformées
├── src/
│   └── ingest.py  # Script d'ingestion des taux de change
├── .env           # Clé API (non versionné)
├── requirements.txt
└── README.md
```