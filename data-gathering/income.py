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
COLUMNS = ['ZipCode', 'Community', 'EstimatedMedianIncome']

# Initialize dataset
result = defaultdict(list)

# Extract webpage
webpage = get(
    url = 'http://www.laalmanac.com/employment/em12c.php',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Extract data
table = soup.find_all('tr')
for row in table:
    details = row.find_all('td')
    for idx, detail in enumerate(details):
        result[COLUMNS[idx]].append(detail.text.strip())

# Save data
mhi_19_data = DataFrame(result)
mhi_19_data.to_csv('dataset/median_household_income_2019.csv')