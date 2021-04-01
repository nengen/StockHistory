# stockstory

Script for retrieving historical stock prices

## Usage
Examples

Scrape one ticker
'''
python3 main.py -t TICKER
'''

Scrape a list of tickers
'''
python3 main.py -tl TICKERLIST
'''

Scraping from - to a specific date
'''
python3 main.py -tl stocks.txt -fd 2020-01-01 -td 2020-12-31
'''



## Notes
I have not implemented any safeguards, make sure the following is followed.
Date format: YYYY-MM-DD
Ticker list: should be a file containing a list with one ticker pr line