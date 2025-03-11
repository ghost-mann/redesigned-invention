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

    def update_economic_calender(self, api_key=None):
        """
            Fetch upcoming economic indicators that affect gold
            Can connect to providers like Alpha Vantage, Trading Economics, or Investing.com
        """
        # example implementation with a hypothetical API
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        next_week = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

        # filter for indicators that impact gold" inflation, interest rates, employment
        gold_impact_indicators = ['CPI', 'PPI', 'Interest Rate Decision','Non-Farm Payrolls', 'PCE']

        url = f"https://economiccalendar-api.example.com/events?from={today}&to={next_week}&api_key={api_key}"
        # In a real implementation, replace with actual API\

        # plcaeholder for API response
        response_data = {
            "events": [
                {
                    "date": "2025-03-13", "time": "08:30", "country": "US", "indicator": "CPI m/m",
                    "impact": "high", "forecast": "0.3%", "previous": "0.2%"
                }
            ]
        }

        # convert to df with importance weights for gold
        events_df = pd.DataFrame(response_data["events"])

        # add gold impact score(1-10 scale)
        events_df["gold impact score"] = events_df["indicator"].apply(self._calculate_gold_impact)

        # save the df as instance variable making it accessible elsewhere in the class
        self.economic_calender = events_df
        return events_df