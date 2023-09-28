# -*- coding: utf-8 -*-
"""

get historical option price data in python with polygon.io API
@author: adam getbags

"""


# pip OR conda install
# pip install polygon-api-client
# pip install plotly

# import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd

from polygonAPIkey import polygonAPIkey
client = RESTClient(polygonAPIkey)  # api_key is used

# for c in RESTClient.list_tickers():
#     print(c)

contractNames = []
# for c in client.list_options_contracts(underlying_ticker='AAPL', limit=1000):
for c in client.list_options_contracts(underlying_ticker='XSP', limit=1000):
    contractNames.append(c)
    print(c)
    print()

print(contractNames)
