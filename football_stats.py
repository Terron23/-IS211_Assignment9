import urllib2
from bs4 import BeautifulSoup
import json
import ssl

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns' 
context = ssl._create_unverified_context()
page = urllib2.urlopen(url, context=context)
soup = BeautifulSoup(page.read(), features="html.parser")
print("\n[\"Player\", \"Position\", \"Touchdowns\", \"Team\"]")
def NFLPlayerStats():
    touchdown_list = []
    fhandler = soup.find_all(class_= {'row1', 'row2'})

    for touchdowns in fhandler[:20]:
        try:
            player = touchdowns.contents[0].get_text()
            position = touchdowns.contents[1].get_text()
            touch_downs = touchdowns.contents[6].get_text()
            team = touchdowns.contents[2].get_text()
            tdplayers = (player, position, touch_downs, team)
            print(json.dumps(tdplayers))

        except:
            print 'Bad URL'
            continue

    return touchdown_list

if __name__ == "__main__":
    NFLPlayerStats()