def stock_price_ratios(entry, real_life):
    ratios = []
    close_data = real_life[0:5]
    for index in range(len(close_data)-1):
        ratios.append(close_data[index+1]/close_data[index])
    return ratios
