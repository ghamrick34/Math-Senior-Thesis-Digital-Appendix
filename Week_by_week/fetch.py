# Import Yahoo! finance tools
import yfinance as yf

# Import the MatLab plotting library
import matplotlib.pyplot as plt

# What stock?
#stock_input = "plug"
#stock_input = input("Enter stock ticker: ")

# Format
def stock(entry):
    ticker = entry.upper()
    return ticker

# Fetch the data for the stock

def data(entry):
    ticker = entry.upper()
    history = yf.Ticker(ticker).history("5y")
    return history

def close_data(entry):
    ticker = entry.upper()
    history = yf.Ticker(ticker).history("5y")
    return history['Close']

def open_data(entry):
    ticker = entry.upper()
    history = yf.Ticker(ticker).history("5y")
    return history['Open']

# print(history)

# print(close_data())
# print(close_data()[-2])