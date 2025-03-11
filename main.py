import pandas as pd
import requests
import datetime
from forex_python.converter import CurrencyRates

# data organisation and storage
class MarketInfluenceTracker:
    def __init__(self):
        self.economic_calender = pd.DataFrame()
        self.central_bank_events = pd.DataFrame()
        self.geopolitical_events = pd.DataFrame()
        self.sentiment_indicators = pd.DataFrame()
        self.seasonal_events = pd.DataFrame()

    def initalize_seasonal_patterns(self):
        seasonal = [
            {"event": "Chinese New Year", "impact": "high", "effect": "positive",
             "start_month": 1, "start_day": 21, "end_month": 2, "end_day": 20, "duration_days": 15},
            {"event": "Indian Wedding Season", "impact": "medium", "effect": "positive",
             "start_month": 10, "start_day": 15, "end_month": 12, "end_day": 15, "duration_days": 60},
            {"event": "Diwali", "impact": "high", "effect": "positive",
             "start_month": 10, "start_day": 15, "end_month": 11, "end_day": 15, "duration_days": 5},
        ]

        return pd.DataFrame(seasonal)
