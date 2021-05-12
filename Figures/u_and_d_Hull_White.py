import stock_price_ratios
import statistics as stat

stock_price_ratios = stock_price_ratios.stock_price_ratios()

sample_mean = stat.mean(stock_price_ratios)

sample_standard_deviation = stat.stdev(stock_price_ratios)

def u():
    return sample_mean + sample_standard_deviation
# print("U = " + str(u()))

def d():
    return sample_mean - sample_standard_deviation
# print("D = " + str(d()))
