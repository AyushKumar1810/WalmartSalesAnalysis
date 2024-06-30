import os
from analyze_city_branch import analyze_city_branch_sales
from average_price import average_price
from month_over_month_analysis import month_over_month_analysis
from generate_report import generate_report

def main():
    filepath = os.path.abspath(os.path.join('..', 'data', 'Walmart_Sales.csv'))
    analyze_city_branch_sales(filepath)
    average_price(filepath)
    month_over_month_analysis(filepath)
    generate_report()

if __name__ == "__main__":
    main()
