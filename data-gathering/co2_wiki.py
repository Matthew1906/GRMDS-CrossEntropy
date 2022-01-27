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
COLUMNS = [
    'rank', 'jurisdiction', 
    'Annual CO2 Emissions in 2017 (millions of metric tons)',
    'Emission Percentage', 'Population','Population Percentage',
    'Annual emission per capita (metric tons)', 
    'emmisions in 2017 per 1000 square miles (millions of metric tons)'
]

# Initialize dataset
result = defaultdict(list)

# Extract webpage
webpage = get(
    url = 'https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_carbon_dioxide_emissions',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Extract data
table = soup.select('.wikitable tbody tr')
for index,row in enumerate(table[3:]):
    details = row.find_all('td')
    for idx, detail in enumerate(details):
        result[COLUMNS[idx]].append(detail.text.strip())

# Save data
co2_data = DataFrame(result).drop('rank', axis='columns')
co2_data.to_csv('dataset/co2_wiki.csv')