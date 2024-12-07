import pandas as pd
import numpy as np

def etl_process(input_file='../Data/financial_data_before_etl.csv', output_file='../Data/financial_data_after_etl.csv'):
    # Load the data (Extract)
    data_raw = pd.read_csv(input_file, parse_dates=['Date'])

    # Calculate daily returns (Transform)
    data_raw['Returns'] = data_raw['Stock Price'].pct_change()

    # Calculate risk metrics: Moving average and standard deviation (for volatility)
    data_raw['Moving Average'] = data_raw['Stock Price'].rolling(window=20).mean()
    data_raw['Risk'] = data_raw['Returns'].rolling(window=20).std() * np.sqrt(252)  # Annualized risk

    # Drop missing values
    data_clean = data_raw.dropna()

    # Save the transformed data (Load)
    data_clean.to_csv(output_file, index=False)
    print(f"Transformed data saved to '{output_file}'")
    return data_clean

if __name__ == "__main__":
    etl_process()
