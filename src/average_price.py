import pandas as pd
import os

def average_price(filepath):
    df = pd.read_csv(filepath)
    average_prices = df.groupby(['City', 'Branch'])['Unit price'].mean().reset_index()
    output_path = os.path.join('..', 'results', 'average_price.csv')
    average_prices.to_csv(output_path, index=False)
    return average_prices

if __name__ == "__main__":
    filepath = os.path.abspath(os.path.join('..', 'data', 'Walmart_Sales.csv'))
    average_price(filepath)
