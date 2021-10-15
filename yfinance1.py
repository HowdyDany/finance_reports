import yfinance as yf
import pandas as pd

ticker = "msft"
ticker = ticker.upper()

company = yf.Ticker(ticker)

week_hist = company.history(period="5d")

print(week_hist)
