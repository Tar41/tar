import yfinance as yf
import matplotlib.pyplot as plt


def q05():
    # Step 1: Define the stock tickers and the start date
    stocks = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']  # Apple, Walmart, IBM, Micron Technology, Boeing, American Express
    start_date = '2024-01-01'

    # Step 2: Download the stock data
    data = yf.download(stocks, start=start_date)['Adj Close']

    # Step 3: Plot the adjusted close prices
    plt.figure(figsize=(10, 7))  # Set figure size to 10 x 7 inches
    data.plot()

    # Step 4: Add chart decorations
    plt.title('Adjusted Close Prices of Stocks since 1st Jan 2024')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price (USD)')

    # Step 5: Save and show the line chart
    plt.tight_layout()
    plt.savefig('plot05.png', format='png')  # Save as plot05.png
    plt.show()  # Show the chart