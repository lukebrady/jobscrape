import requests, re

from bs4 import BeautifulSoup

# Nasa Jobs URL.
url = "https://www.usajobs.gov/Search?d=NN"

jobs = requests.get(url).text

soup = BeautifulSoup(jobs, 'html.parser')

patt = re.compile('Computer Scientist*')

