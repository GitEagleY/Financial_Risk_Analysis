import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(input_file='../Data/financial_data_after_etl.csv'):
    # Load the cleaned data
    data_clean = pd.read_csv(input_file, parse_dates=['Date'])

    # Set up the Seaborn style
    sns.set(style="whitegrid")

    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Stock Price over Time
    axes[0, 0].plot(data_clean['Date'], data_clean['Stock Price'], label='Stock Price', color='blue')
    axes[0, 0].set_title('Stock Price Over Time')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Price')

    # Trading Volume Over Time
    axes[0, 1].plot(data_clean['Date'], data_clean['Trading Volume'], label='Trading Volume', color='green')
    axes[0, 1].set_title('Trading Volume Over Time')
    axes[0, 1].set_xlabel('Date')
    axes[0, 1].set_ylabel('Volume')

    # Returns Histogram
    axes[1, 0].hist(data_clean['Returns'].dropna(), bins=50, color='purple', edgecolor='black')
    axes[1, 0].set_title('Returns Distribution')
    axes[1, 0].set_xlabel('Returns')
    axes[1, 0].set_ylabel('Frequency')

    # Risk (Volatility) Over Time
    axes[1, 1].plot(data_clean['Date'], data_clean['Risk'], label='Risk (Volatility)', color='red')
    axes[1, 1].set_title('Risk (Volatility) Over Time')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('Risk')

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

def risk_metrics(input_file='../Data/financial_data_after_etl.csv'):
    # Load the cleaned data
    data_clean = pd.read_csv(input_file)

    # Value at Risk (VaR) at 95% confidence level
    VaR_95 = data_clean['Returns'].quantile(0.05)

    # Conditional Value at Risk (CVaR)
    CVaR_95 = data_clean[data_clean['Returns'] <= VaR_95]['Returns'].mean()

    print(f"Value at Risk (95%): {VaR_95}")
    print(f"Conditional Value at Risk (95%): {CVaR_95}")

if __name__ == "__main__":
    visualize_data()
    risk_metrics()
