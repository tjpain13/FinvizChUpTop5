import urllib.request
from bs4 import BeautifulSoup
import os
import datetime

# Pull HTML from finviz channel up page, parse
url = "https://finviz.com/screener.ashx?v=150&s=ta_p_channelup"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                         "Version/14.0.3 Safari/605.1.15"}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

# Sort for pertinent html
tags = soup.find_all("a", "screener-link-primary", limit=5)

# Pull relevant text only out of html
top5 = []
for t in tags:
    top5.append(t.text)

# check if save file exists for ticker data - if not, create a .json file and adds ticker name and
# date of addition to the first two lines, respectively, upon creation

curdt = datetime.date.today()
path = "/Your/Path/Here/"  # add your desired path here, INCLUDE trailing "/" or "\"

for o in top5:
    if not os.path.exists(f'{path}{o}.json'):
        f = open(f'{path}{o}.json', 'a')
        f.write(f'{o}\n{curdt}')
        f.close()
