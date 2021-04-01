import argparse
from scraper import Scraper
from datetime import date

parser = argparse.ArgumentParser(description='Fetch stock data')
parser.add_argument('-fd', type=str, help='Optional - From date in YYYY-MM-DD format. Defaults to 1900-01-01', dest='fd', default=0)
parser.add_argument('-td',  type=str, help='Optional - specify to date in YYYY-MM-DD. Defaults to current date', dest='td',default=0)
parser.add_argument('-t', type=str, help='ticker to scrape', dest='ticker',default=0)
parser.add_argument('-tl',  type=str, help ='file containting a list of all tickers', dest='ticker_list', default=0)

args = parser.parse_args()

def process_tickers(ticker, ticker_list):
    if ticker == 0 and ticker_list == 0:
        print ("No tickers specified")
        return 0
    elif ticker_list == 0:
        return [ticker]
    else:
        with open(ticker_list) as f:
            lines = [line.rstrip() for line in f]
            return lines



def main():
    from_date = args.fd
    to_date = args.td
    ticker = args.ticker
    ticker_list = args.ticker_list
    tickers = process_tickers(ticker, ticker_list)
    if from_date == 0:
        from_date = '1900-01-01'
    if to_date == 0:
        to_date = str(date.today())
    if tickers != 0:
        scraper = Scraper(ticker_list)
        scraper.scrape_historical_stocks(tickers, from_date,to_date)
    else:
        print("Please specify tickers")



main()
