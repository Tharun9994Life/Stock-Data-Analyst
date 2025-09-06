import yfinance as yf
import numpy as np
import datetime as dt
import pandas as pd

class Stock:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        self._data = None

    def _retrieve_stock_data(self, date, stock_data):
        row = stock_data.loc[date]

        return {
            "Date": date.strftime("%d/%m/%Y"),
            "Open": row["Open"],
            "High": row["High"],
            "Low": row["Low"],
            "Close": row["Close"],
            "Adj Close": row["Adj Close"],
            "Volume": row["Volume"]
        }

    def fetch_stock_data_at_specific_date(self, date):
        stock_data = self.ticker.history(period="max", auto_adjust=False)
        stock_data.index = stock_data.index.date
        stock_data = stock_data[["Open", "High", "Low", "Adj Close", "Close", "Volume"]]

        if date not in stock_data.index:
            return None
        return self._retrieve_stock_data(date, stock_data)

    def fetch_stock_data_over_period_of_time(self, start_date, end_date):
        stock_data = self.ticker.history(start=start_date, end=end_date, auto_adjust=False)
        stock_data.index = stock_data.index.date
        stock_data = stock_data[["Open", "High", "Low", "Adj Close", "Close", "Volume"]]
        stock_prices = []
        
        for date in stock_data.index:
            stock_prices.append(self._retrieve_stock_data(date, stock_data))
        return stock_prices

    def returns(self, *, date=None, start_date=None, end_date=None):
        if date:
            current_adjusted_close_price = None
            previous_adjusted_close_price = None
            previous_date = date - dt.timedelta(days=1) 
            
            current_stock = self.fetch_stock_data_at_specific_date(date)
            while (current_stock == None):
                current_date -= dt.timedelta(days=1)
                current_stock = self.fetch_stock_data_at_specific_date(previous_date)
            
            current_adjusted_close_price = current_stock["Adj Close"]

            previous_stock = self.fetch_stock_data_at_specific_date(previous_date)
            while (previous_stock == None):
                previous_date -= dt.timedelta(days=1)
                previous_stock = self.fetch_stock_data_at_specific_date(previous_date)
            
            previous_adjusted_close_price = previous_stock["Adj Close"]
            
            return (current_adjusted_close_price - previous_adjusted_close_price) / previous_adjusted_close_price
    
        elif start_date and end_date:
            adjusted_close_prices = []

            current_stocks = self.fetch_stock_data_over_period_of_time(start_date, end_date)
            for stock in current_stocks:
                if stock:
                    adjusted_close_prices.append(stock["Adj Close"])
            
            adjusted_close_prices = pd.Series(adjusted_close_prices)
            return (1 + adjusted_close_prices.pct_change().dropna()).cumprod() - 1