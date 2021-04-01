import requests
from datetime import datetime
from datetime import timezone
import os.path
from os import path
import csv


class Scraper:

    def __init__(self,tickers):
        self.tickers = tickers

    def scrape_historical_stocks(self,tickers, from_date,to_date):
        ''' returns a csv of historical prices'''
        self.setup()
        dates = self.get_date(from_date,to_date) 
        for ticker in tickers:
            url = 'https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&includeAdjustedClose=true' % (ticker,dates[0],dates[1])
            response = requests.get(url)
            data = response.text.split('\n')
            data.pop(0) # removes header
            self.process_stock(data,ticker)
        print("Data is in stocks.csv.")

    def process_stock(self,data,ticker):
        ''' Write scraped data to csv '''
        with open('stocks.csv', mode='a') as stockfile:
            writer = csv.writer(stockfile, delimiter=',')
            for row in data:
                row = row.split(",")
                row.insert(0,ticker)
                writer.writerow(row)


    def get_date(self, from_date,to_date):
        ''' convert to unix date '''
        fr = datetime.strptime(from_date, '%Y-%m-%d')
        to = datetime.strptime(to_date, '%Y-%m-%d')
        fr_unix = fr.replace(tzinfo=timezone.utc).timestamp()
        to_unix = to.replace(tzinfo=timezone.utc).timestamp()
        return [int(fr_unix),int(to_unix)]

    def setup(self):
        ''' Create stocks.csv file, delete if it already exists '''
        with open('stocks.csv', mode='w+') as stockfile:
            writer = csv.writer(stockfile,delimiter=',')
            writer.writerow(['Ticker','Date','Open','High','Low','Close','Adj_close','Volume'])


