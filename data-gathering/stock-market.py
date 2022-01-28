# ---------------------------- Import modules ---------------------------- 
## Scraping modules
from bs4 import BeautifulSoup
from requests import get
## Data structure
from collections import defaultdict
from pandas import DataFrame
## Debugging
from pyperclip import copy

# Utilities
COLUMNS = ['SECTOR', 'MKT_CAP', 'DIY_YIELD', 'CHG%', 'VOL', 'INDUSTRIES', 'STOCKS']

# Initialize dataset
result = defaultdict(list)

# Extract webpage
webpage = get(
    url = 'https://www.tradingview.com/markets/stocks-usa/sectorandindustry-sector/',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Extract data
table = soup.select('tr.tv-data-table__row')

for row in table:
    details = row.find_all('td')
    for idx, detail in enumerate(details):
        if detail.text.strip()!='':
            result[COLUMNS[idx]].append(detail.text.strip())

# Save data
stock_market_data = DataFrame(result)
stock_market_data.to_csv('dataset/stock_market.csv')