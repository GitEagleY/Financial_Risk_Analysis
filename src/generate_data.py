import pandas as pd
import numpy as np

def generate_data():
    # Number of days (data points)
    n = 365  # 1 year of data

    # Simulate stock prices
    dates = pd.date_range('2023-01-01', periods=n, freq='D')
    stock_prices = np.random.normal(loc=100, scale=20, size=n).cumsum()

    # Simulate trading volume
    trading_volume = np.random.randint(1000, 5000, size=n)

    # Simulate volatility (standard deviation of returns)
    volatility = np.random.normal(loc=0.02, scale=0.01, size=n)

    # Create a DataFrame
    data = pd.DataFrame({
        'Date': dates,
        'Stock Price': stock_prices,
        'Trading Volume': trading_volume,
        'Volatility': volatility
    })

    # Save data to a CSV file
    data.to_csv('../Data/financial_data_before_etl.csv', index=False)
    print("Dummy data generated and saved to 'financial_data_before_etl.csv'")
    return data

if __name__ == "__main__":
    generate_data()
