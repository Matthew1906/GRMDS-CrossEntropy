from tabula import read_pdf
from requests import get

pdf_file = get('https://www.bea.gov/sites/default/files/2021-09/gdp2q21_3rd.pdf')

with open('./assets/temp.pdf', 'wb') as writer:
    writer.write(pdf_file.content)

data = read_pdf('./assets/temp.pdf', pages = '9-28')
print(data)