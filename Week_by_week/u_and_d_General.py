import stock_price_ratios as spr
import statistics as stat
import math


def u(q, entry, real_life):
    stock_price_ratios = spr.stock_price_ratios(entry, real_life)
    sample_mean = stat.mean(stock_price_ratios)
    sample_standard_deviation = stat.stdev(stock_price_ratios)
    return sample_mean + math.sqrt((1-q)/q) * sample_standard_deviation
# print("U = " + str(u()))

def d(q, entry, real_life):
    stock_price_ratios = spr.stock_price_ratios(entry, real_life)
    sample_mean = stat.mean(stock_price_ratios)
    sample_standard_deviation = stat.stdev(stock_price_ratios)
    return sample_mean - math.sqrt(q/(1-q)) * sample_standard_deviation
# print("D = " + str(d()))
