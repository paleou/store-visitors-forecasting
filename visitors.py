import os
import pandas as pd
from prophet import Prophet

# Configuration
DATA_PATH = "data/visitors_history.csv"
OUT_PATH = "results/forecast_2025.csv"

CLOSED_HOLIDAYS = [
    "2025-01-01", "2025-01-02", "2025-01-06", "2025-03-03",
    "2025-03-25", "2025-04-18", "2025-04-21", "2025-05-01",
    "2025-08-15", "2025-10-28", "2025-12-25", "2025-12-26"]
CLOSED_HOLIDAYS = pd.to_datetime(CLOSED_HOLIDAYS)

START_2025 = "2025-01-01"
END_2025 = "2025-12-31"

# Load data
df = pd.read_csv(DATA_PATH, sep=";")
df["Date"] = pd.to_datetime(df["Date"])
df = df.rename(columns={"Date": "ds", "Visitors": "y"}).sort_values("ds")

# Train Prophet model
m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
m.fit(df)

# Forecast 2025
future = pd.date_range(START_2025, END_2025, freq="D")
future_df = pd.DataFrame({"ds": future})
forecast = m.predict(future_df)

# Prepare output
forecast = forecast[["ds", "yhat"]].copy()

# Apply store closures
forecast["weekday"] = forecast["ds"].dt.weekday
forecast["is_closed"] = forecast["ds"].isin(CLOSED_HOLIDAYS) | (forecast["weekday"] == 6)
forecast.loc[forecast["is_closed"], "yhat"] = 0

# --- Save result ---
forecast = forecast.rename(columns={"ds": "Date", "yhat": "VisitorsForecast"}).sort_values("Date")
os.makedirs("results", exist_ok=True)
forecast[["Date", "VisitorsForecast"]].to_csv(OUT_PATH, index=False)
print(f"Forecast file saved to {OUT_PATH}")