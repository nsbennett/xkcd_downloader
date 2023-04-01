import requests
from bs4 import BeautifulSoup
import lxml


for i in range(4000):
    target = f"https://xkcd.com/{i}"

    webpage = requests.get(target)

    try:
        image = bs4.BeautifulSoup.find("meta", property="og:image")
    except:
        continue

