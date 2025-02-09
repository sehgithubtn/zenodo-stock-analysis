import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
csv_filename = "World-Stock-Prices-Dataset.csv"
df = pd.read_csv(csv_filename)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Select Apple Stock Data (Ticker = AAPL)
apple_stock = df[df['Ticker'] == 'AAPL']

# Check if data exists
if apple_stock.empty:
    print("No data found for AAPL. Please check the dataset.")
else:
    # Plot Apple Stock Closing Prices Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(apple_stock['Date'], apple_stock['Close'], label='Apple Stock Price', color='blue', linewidth=2)

    # Formatting
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Closing Price (USD)", fontsize=12)
    plt.title("Apple Stock Price Over Time", fontsize=14)
    plt.legend()
    plt.grid(True)

    # Save the plot
    plot_filename = "stock_plot.png"
    plt.savefig(plot_filename)
    print(f"Plot saved as: {plot_filename}")

    # Show the plot
    plt.show()
