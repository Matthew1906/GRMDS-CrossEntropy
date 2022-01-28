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
COLUMNS = ['State', 'GasolineTax', 'DieselTax', 'AviationFuelTax', 'JetFuelTax']
filter_data = lambda x: 0 if x.strip() == 'no tax' else x.strip()

# Initialize dataset
result = defaultdict(list)

# Extract webpage
webpage = get(
    url = r'https://igentax.com/gas-tax-state/#:~:text=Gas%20Tax%20by%20State%20%20%20%20State,%20no%20tax%20%2023%20more%20rows%20',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Extract data
table = soup.select('tr')

for row in table:
    details = row.select('td')
    for idx, detail in enumerate(details):
        result[COLUMNS[idx]].append(filter_data(detail.text))

# Save data
gt_data = DataFrame(result)
gt_data.to_csv('dataset/gasoline_tax.csv')