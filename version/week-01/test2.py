from Stock import Stock
import matplotlib.pyplot as plt
import pandas as pd

stock1 = Stock("AAPL")

date1 = "2025-08-19"
date1 = pd.to_datetime(date1).date()

date2 = "2025-08-30"
date2 = pd.to_datetime(date2).date()

stock_prices = stock1.fetch_stock_data_over_period_of_time(date1, date2)
stock_price_returns = stock1.returns(start_date=date1, end_date=date2)

x = []
y = []

for stock_price in stock_prices:
    x.append(stock_price["Date"])
    y.append(stock_price["Open"])
    
    print(f"Date: {stock_price['Date']}")
    print(f"Open Price: {stock_price['Open']}")
    print(f"High Price: {stock_price['High']}")
    print(f"Low Price: {stock_price['Low']}")
    print(f"Close Price: {stock_price['Close']}")
    print(f"Adjusted Close Price: {stock_price['Adj Close']}")
    print(f"Volume: {stock_price['Volume']}")

print(f"Returns: {100 * stock_price_returns}%")
    
plt.plot(x, y)
plt.show()