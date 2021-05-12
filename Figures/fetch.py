# Import Yahoo! finance tools
import yfinance as yf

# Import the MatLab plotting library
import matplotlib.pyplot as plt

# What stock?
stock_input = input("Enter stock ticker: ")

# Format
ticker = stock_input.upper()
def stock():
    return ticker

# Fetch the data for the stock
history = yf.Ticker(ticker).history("5y")

def data():
    return history

def close_data():
    return history['Close']

def open_data():
    return history['Open']