# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:44:24 2020

@author: Lakshmikanth

Reference from https://blog.quantinsti.com/capital-asset-pricing-model/
"""

from nsepy import get_history
from datetime import datetime , date

import dateutil.relativedelta
import pandas as pd
import statsmodels.api as sm

stock_symbol = 'RELIANCE'
index_symbol = 'NIFTY'

# Linear regression
def linregression(x,y):
    model = sm.OLS(x,y).fit()
    predictions = model.predict(x)
    print_model = model.summary()
    return print_model

to_date = datetime.now()
to_date = datetime.strftime(to_date, '%Y,%m,%d %H,%M,%S')
to_date = datetime.strptime(to_date, '%Y,%m,%d %H,%M,%S')
from_date = to_date-dateutil.relativedelta.relativedelta(months = 12)

stock_history = get_history(symbol=stock_symbol, 
                   start =from_date , 
                   end = to_date)
index_history = get_history(symbol=index_symbol, 
                   start =from_date , 
                   end = to_date ,
                   index=True)
closing_prices = pd.concat([stock_history['Close'] ,index_history['Close'] ], axis=1)
closing_prices.columns = [stock_symbol, index_symbol]
print(closing_prices.head())

output = linregression(closing_prices.RELIANCE , closing_prices.NIFTY)
print(output)


