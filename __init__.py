import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

quandl.ApiConfig.api_key = '9Mj_SA7bCxBrUSssNpHL'
dow_jones = ['MMM', 'AXP' 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DD', 'XOM', 'GE', 
             'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 
             'TRV', 'UTX', 'UNH', 'VZ', 'V', 'WMT']
             
