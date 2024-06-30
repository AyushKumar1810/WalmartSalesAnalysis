import pandas as pd
import os

def analyze_city_branch_sales(filepath):
    df = pd.read_csv(filepath)
    df['Total'] = df['Unit price'] * df['Quantity']
    city_branch_sales = df.groupby(['City', 'Branch']).agg({'Total': 'sum'}).reset_index()
    output_path = os.path.join('..', 'results', 'city_branch_sales.csv')
    city_branch_sales.to_csv(output_path, index=False)
    return city_branch_sales

if __name__ == "__main__":
    filepath = os.path.abspath(os.path.join('..', 'data', 'Walmart_Sales.csv'))
    analyze_city_branch_sales(filepath)
