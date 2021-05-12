import fetch
import pandas as pd

renewable = ["run","fslr","cwen","nee","tsla","plug"]
fossil = ["xom","cvx","btu","arch","cop"]

for stock in renewable:
    fetch.close_data(stock).to_csv(stock+'.csv')

for stock in fossil:
    fetch.close_data(stock).to_csv(stock+'.csv')