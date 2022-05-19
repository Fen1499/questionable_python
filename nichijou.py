from bs4 import BeautifulSoup
import requests

page_html = requests.get("https://nichijou.fandom.com/wiki/Interstitials")
page_soup = BeautifulSoup(page_html.text, 'html.parser')

imgs = page_soup.main.find_all('img')
links = [i.get('src', '') for i in imgs]

for link in links:
    if (pos := link.find('.png')) > -1:
        png_link = link[:pos+4]
        print(png_link[-13:])
        response = requests.get(png_link)
        with open(png_link[-13:], 'wb') as file:
            file.write(response.content)
