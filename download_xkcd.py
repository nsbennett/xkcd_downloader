# NOT YET READY TO USE

import requests
from bs4 import BeautifulSoup
import lxml


for i in range(4000):
    target = f"https://xkcd.com/{i}"

    webpage = requests.get(target)

    try:
        image = BeautifulSoup.find("meta", property="og:image")
    except:
        continue
BeautifulSoup.select()
