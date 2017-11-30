# Stock Market Predictors
Download: [Data](https://www.quandl.com/product/WIKIP/WIKI/PRICES-Quandl-End-Of-Day-Stocks-Info), [Documentation](https://www.quandl.com/product/WIKIP/documentation/about)

Abstract: Label each stock Buy, Hold, or Sell based on particular metrics and past performance.

## Attribute Information:
List of original attributes: 
- `ticker`: An arrangement of characters (usually letters) representing a particular security listed on an exchange or otherwise traded publicly.
- `date`: Date the data was collected.
- `open`: The price of the first trade for any listed stock on a given date. 
- `high`: The highest price at which a stock traded during the course of the day. 
- `low`: The lowest price at which a stock traded during the course of the day.
- `close`: The final price at which a stock is traded on a given trading day.
- `volume`: The number of shares of a stock that changed hands during a given day.
- `ex-dividend`: The time period between the announcement and payment of a dividend.
- `split_ratio`: The ratio of shares outstanding compared to what was originally available before a stock split.
- `adj_open`: The stock's opening price on any given day of trading that has been amended to include any distributions and corporate actions that occurred.
- `adj_high`: The stock's highest trading price on any given day of trading that has been amended to include any distributions and corporate actions that occurred.
- `adj_low`: The stock's lowest trading price on any given day of trading that has been amended to include any distributions and corporate actions that occurred.
- `adj_close`: The stock's closing price on any given day of trading that has been amended to include any distributions and corporate actions that occurred at any time prior to the next day's open.
- `adj_volume`: The number of shares of a stock that changed hands on any given day of trading that has been amended to include any distributions and corporate actions that occurred.

## Problem Statement


## Solution Statement


## Benchmark Model


## Performance Metric


## Project Roadmap
1. Gather and store data

    Link to data: https://www.quandl.com/product/WIKIP/WIKI/PRICES-Quandl-End-Of-Day-Stocks-Info
    
```
.
├── README.md
├── __indicators__.py
├── __init__.py
├── data
│   ├── disney_df.p
│   ├── dow_jones_df.p
│   └── dow_jones_df_daymonthyear.p
└── ipynb
    ├── dow_jones_table.ipynb
    └── stock_eda.ipynb
```

2. Feature Engineering
    - https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code
    - chose following n values:
        - 5, number of trading days per week
        - 21, number of trading days per month
        - 63, number of trading days per quarter
        - 125, number of trading days per two quarters
        - 250, number of trading days per year
        
    - Added Metrics:
        - [5, 21, 63, 125, 250]-Day Moving Average (MA)
        - [5, 21, 63, 125, 250]-Day Exponential Moving Average (EMA)
        - [5, 21, 63, 125, 250]-Day Momentum (MOM)
        - [5, 21, 63, 125, 250]-Day Rate of Change (ROC)
        - [5, 21, 63, 125, 250]-Day Bollinger Bands (BBANDS)
        - Pivot Points, Supports and Resistances (PPSR)
        - Stochastic Oscillator %K (STOK)
        - [5, 21, 63, 125, 250]-Day Stochastic Oscillator %D (STO)
        - Mass Index (MassI)
        - [5, 21, 63, 125, 250]-Day Accumulation/Distribution (ACCDIST)
        - Chaikin Oscillator (Chaikin)
        - [5, 21, 63, 125, 250]-Day Force Index (FORCE)
        - [5, 21, 63, 125, 250]-Day Ease of Movement (EOM)
        - [5, 21, 63, 125, 250]-Day Commodity Channel Index (CCI)
        - [5, 21, 63, 125, 250]-Day Coppock Curve(COPP)
        - [5, 21, 63, 125, 250]-Day Keltner Channel (KELCH)
        - [5, 21, 63, 125, 250]-Day Standard Deviation (STDDEV)
        
        
    - TODO: 
        - Try to fix warnings
        - [5, 21, 63, 125, 250]-Day Average True Range (ATR): not working
        - [5, 21, 63, 125, 250]-Day Trix (TRIX): not working
        - Average Directional Movement Index (ADX): not sure what input values 
        - MACD, MACD Signal and MACD difference (MACD): not sure what input values
        - [5, 21, 63, 125, 250]-Day Vortex Indicator (Vortex): not working
        - KST Oscillator (KST): not sure what input values
        - [5, 21, 63, 125, 250]-Day Relative Strenght Index (RSI): not working
        - True Strenght Index (TSI): not sure what input values
        - [5, 21, 63, 125, 250]-Day Money Flow Index and Ratio (MFI): not working
        - [5, 21, 63, 125, 250]-Day On-balance Volume (OBV): not working
        - Ultimate Oscillator (ULTOSC): not working
        - [5, 21, 63, 125, 250]-Day Donchian Channel (DONCH): not working

1. Establish sampling procedure

1. EDA - data cleaning

1. EDA - statistics

1. Establish performance metric 

1. EDA

1. Benchmark Model

1. Standardize Data

1. Skew-Normalize Data

1. Investigate outliers
   - box plot
   
1. Bias-Variance Tradeoff in sample size

1. Principal Component Analysis

1. Examine Scree Plot

1. Segmentation

1. Feature selection

1. Develop model pipelines

1. Gridsearch model pipelines

## Stretch Goals
1. Explore individual feature relevance

1. Reduce the feature set

1. Explore other data projections:
   - Polynomial expansions