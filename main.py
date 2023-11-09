import requests
import json
from bs4 import BeautifulSoup as bs

def Scrape(url):
    res = requests.get(url)

    if res.status_code == 200:
        html = res.text
        soup = bs(html, 'html.parser')

        parentElement = soup.find_all('div', class_="carousel-block-table prakicu-kota")

        data_result = []

        for element in parentElement:
            data = {}

            data['kota'] = element.find('h2', class_='kota').text
            data['waktu'] = element.find('p').text.replace('\xa0', ' ')
            data['cuaca'] = element.find('img')['alt']
            data['suhu'] = element.find('h2', class_='heading-md').text

            data_result.append(data)


        with open('data.json', 'w') as file:
            json.dump(data_result, file)
            print('done')


url = 'https://www.bmkg.go.id/'

Scrape(url)