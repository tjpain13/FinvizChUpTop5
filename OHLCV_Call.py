# returns ohlccv data from yahoo finance historical data page, separated by "|"
# roughly the same process as is used in Maker

import urllib.request
from bs4 import BeautifulSoup


def ohlccv_output(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    ohlcvraw = soup.find_all("td", "Py(10px)", limit=7)
    ohlcv = []
    for o in ohlcvraw:
        ohlcv.append(o.text)
    ohlcvfinal = ('|'.join(ohlcv))
    return ohlcvfinal

