#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

# report.py
import csv
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        portfolio = fileparse.parse_csv(f, types=[str,int,float])

    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)
    '''
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as f:
        prices = fileparse.parse_csv(f, has_headers=False, types=[str,float])
    prices = dict(prices)

    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    '''
    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    output = '%10s %10s %10s %10s\n' % headers
    output += ('-' * 10 + ' ') * len(headers)
    output += "\n"
    output += "\n".join(['%10s %10d %10.2f %10.2f' % row for row in report])
    return output
    

def portfolio_report(portfolio, prices):
    # Read data files and create the report data        
    portfolio = read_portfolio(portfolio)
    # Generate the report data
    prices    = read_prices(prices)
    report    = make_report_data(portfolio, prices)
    # Output the report
    output = print_report(report)
    print(output)


def main(args):
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
