# summary-api

A tiny FastAPI service that summarizes text. Includes a `/summarize` endpoint that returns a short summary and basic word-count stats. Built as a lightweight practice project to learn AI-assisted development.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn main:app --reload
```
