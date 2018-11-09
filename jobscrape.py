#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import re
import requests
from bs4 import BeautifulSoup


# Check to see if the Job site has an open SRE position.
def checkJobSite(url):
    # Request the DuckDuckGo jobs page.
    ddg_jobs = requests.get(url)
    # Get the text from the webpage.
    soup = BeautifulSoup(ddg_jobs.text, 'html.parser')
    # Strip all the HTML tags from the web content.
    text = soup.get_text()
    # Find all instances of Site Reliability Engineer.
    reg = re.compile('Site Reliability Engineer*')
    result = reg.findall(text)
    return result


if __name__ == '__main__':
    result = checkJobSite("http://app.jazz.co/widgets/basic/create/duckduckgo")
    if len(result) > 0:
        print("DuckDuckGo has an open SRE position.")
    else:
        print("There is not an open position. Check back soon!")
