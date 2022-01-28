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
COLUMNS = ['Component', 'Rank', 'EPI Score', '10-year change']
filter_data = lambda x: None if x.strip() == '-' else x.strip()

# Initialize dataset
result = defaultdict(list)

# Extract webpage
webpage = get(
    url = 'https://epi.yale.edu/epi-results/2020/country/usa',
    headers= {
        'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
)

# Create soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# Extract data
table = soup.select('table')[0]
rows = table.select('tr')

for row in rows:
    details = row.find_all('td')
    for idx, detail in enumerate(details):
        result[COLUMNS[idx]].append(filter_data(detail.text))

# Save data
env_performance_data = DataFrame(result)
env_performance_data.to_csv('dataset/environment_performance.csv')