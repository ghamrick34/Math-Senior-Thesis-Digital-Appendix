import fetch

close_data = fetch.close_data()

ratios = []
for index in range(len(close_data)-1):
    ratios.append(close_data[index+1]/close_data[index])

def stock_price_ratios():
    return ratios
