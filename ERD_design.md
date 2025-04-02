# ERD Design and Use Cases

The ERD diagram was designed with the use cases below in mind. The ERD diagram was set up for analysis of recurring stocks, price movements, and volume trends.
- The **STOCKS** table is the source of the raw candlestick data that is both provided and gathered over many weeks.
- The intermediate tables, **PRICE_RANGES** and **VOLUME_RANGES**, were designed to track price and volume changes over time.
- The intermediate tables, **RECURRING_STOCKS**, **VOLATILE_STOCKS** and **STEADY_STOCKS**, identify patterns and volatility in stock performance. 


## Use Cases
The ERD supports the following stock analysis use cases:

1. **Recurring Stocks**
   - Identifies stocks that appear frequently in the datasets
   - Tracks the number of times a stock symbol repeats over a given period

2. **Volatile Stocks**
   - Detects stocks with significant price fluctuations
   - Computes maximum and average intraday and weekly price changes to measure daily and weekly volatility

3. **Steady Stocks**
   - Identifies stocks with minimal price fluctuations
   - Computes minimum and average intraday and weekly price changes to measure daily and weekly stability.

4. **Price Ranges**
   - Tracks daily and weekly price variations
   - Calculates the range (high - low) for each stock on a daily and weekly basis

5. **Volume Ranges**
   - Measures daily and weekly volume variations
   - Tracks daily and weekly volume changes
