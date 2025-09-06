from Stock import Stock
import pandas as pd

stock1 = Stock("AAPL")

date1 = "2025-08-20"
date1 = pd.to_datetime(date1).date()

stock_price_data = stock1.fetch_stock_data_at_specific_date(date1)
stock_price_returns = stock1.returns(date=date1)

print(f"Date: {stock_price_data['Date']}")
print(f"Open Price: {stock_price_data['Open']}")
print(f"High Price: {stock_price_data['High']}")
print(f"Low Price: {stock_price_data['Low']}")
print(f"Close Price: {stock_price_data['Close']}")
print(f"Adjusted Close Price: {stock_price_data['Adj Close']}")
print(f"Volume: {stock_price_data['Volume']}")
print(f"Returns: {100 * stock_price_returns}%")