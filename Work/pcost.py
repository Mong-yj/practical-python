#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

# pcost.py
import csv
import report
import sys


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    portfolio = report.read_portfolio(filename)

    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)
    '''
    total_cost = sum(row['shares']*row['price'] for row in portfolio)
    return total_cost

def main(args):
    if len(args) != 2:
        print('Usage: %s portfoliofile' % args[0])
        sys.exit()
    cost = portfolio_cost(args[1])
    print("Total cost:",cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)