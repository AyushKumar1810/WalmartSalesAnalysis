import pandas as pd
import os
import matplotlib.pyplot as plt

def month_over_month_analysis(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Month'] = df['Date'].dt.to_period('M')
    df['Total'] = df['Unit price'] * df['Quantity']
    monthly_analysis = df.groupby(['Month', 'Product line', 'Gender', 'Payment']).agg({'Total': 'sum'}).reset_index()
    output_path = os.path.join('..', 'results', 'month_over_month_analysis.csv')
    monthly_analysis.to_csv(output_path, index=False)
    
    # Plot sales trends
    sales_trends = df.groupby('Month')['Total'].sum()
    plt.figure(figsize=(10, 5))
    sales_trends.plot(kind='line')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    sales_trends_path = os.path.join('..', 'visualizations', 'sales_trends.png')
    plt.savefig(sales_trends_path)
    plt.close()
    
    # Plot revenue trends (using 'Total' as a proxy for revenue here)
    revenue_trends = df.groupby('Month')['Total'].sum()
    plt.figure(figsize=(10, 5))
    revenue_trends.plot(kind='line', color='green')
    plt.title('Revenue Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.grid(True)
    revenue_trends_path = os.path.join('..', 'visualizations', 'revenue_trends.png')
    plt.savefig(revenue_trends_path)
    plt.close()

    return monthly_analysis

if __name__ == "__main__":
    filepath = os.path.abspath(os.path.join('..', 'data', 'Walmart_Sales.csv'))
    month_over_month_analysis(filepath)
