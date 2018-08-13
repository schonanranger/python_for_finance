#yahoo的API弃用

import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
start = datetime.datetime(2016, 1, 1) # or start = '1/1/2016'
end = datetime.date.today()
prices = web.DataReader('^GSPC', 'yahoo', start, end)
print(prices.head()) # print first rows of the prices data

