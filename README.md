Overview:
- Forecast of the store's daily visitors for the entire year of 2025.
- Using three years (2022–2024) of historical data from file "visitors_history.csv".
- Automatically sets visitor counts to zero on store-closure dates (Sundays & predefined holidays).
- Modular design with a clean fallback mechanism (Nixtla → Prophet → SARIMAX).
- Designed for easy deployment and automation on GCP.

Running Locally:
- Install dependencies: pip install -r requirements.txt
- Place your visitors_history.csv in the "data" folder.
- Run the forecast script: python src/forecast_2025.py
- The output forecast_2025.csv will be created in the "results" folder.

This project can also be deployed and automated on GCP:
- Cloud Storage → Store raw data (visitors_history.csv) and forecast outputs.
- Cloud Run → Run the forecasting script as a scheduled job.
- BigQuery → Store forecasts for downstream analytics or dashboards.
- Vertex AI → Train and serve Nixtla models in a managed environment.
- Airflow → Orchestrate periodic runs.

Panagiotis Leousis 31/10/2025
