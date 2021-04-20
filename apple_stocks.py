import urllib2
from bs4 import BeautifulSoup
import json
import ssl


url = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
context = ssl._create_unverified_context()
page = urllib2.urlopen(url, context=context)
soup = BeautifulSoup(page.read())

def yahoo_apple_stock():
    data = []
    fhandler = soup.find_all('tr')

    for rows in fhandler:
        try:
            if len(rows.find_all(('td', {'class': 'span data-reactid'}))) == 7:
                date = rows.contents[0].get_text()
                close = rows.contents[5].get_text()
                data.append((date, close))
                json_string = {
                "Date": date,
                "Closed Stock Price": close,
                }
                print(json.dumps(json_string))
        except:
            print 'bad url'
            continue
    return yahoo_apple_stock
    

if __name__ == "__main__":
    yahoo_apple_stock()