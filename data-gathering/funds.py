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
COLUMNS = ['Ticker', 'Fund Name', 'Fund Type', 'Inception Month',
'AUM (US$ millions)', 'YTD %', '1 yr Avg%', '3 yr Avg %', 
'5 yr Avg %', '10 yr Avg%', 'Prev Yr Rtn %', 'Mgmt Fee %', 
'Exp Ratio %', 'Std', 'Dev', 'Benchmark Used']

filter_data = lambda x: None if x.strip() == '--' else x.strip()

# Initialize dataset
result = defaultdict(list)

# Extract Webpage
webpage = get(
    url = 'https://charts.ussif.org/mfpc/',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Select Tags
table = soup.select('#FinancialPerformance tr')
clean_table = [row for row in table if row.get('class') in [None, ['GreyBkg']]]

# Create dataset
for index,row in enumerate(clean_table):
    details = row.find_all('td')
    for idx, detail in enumerate(details):
        result[COLUMNS[idx]].append(filter_data(detail.text))

# Save data
fund_data = DataFrame(result)
fund_data.to_csv('dataset/funds.csv')