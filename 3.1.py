
#парсим первые N страниц недвижки у domclik, по аналогии с примером который кидался. считаем средню цену на всех страницах

import requests
res = ["https://realty.domclick.ru/prodazha-kvartir/?region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1&price__lte=5000000",
       "https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&offset=30&price__lte=5000000&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1",
       "https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&offset=120&price__lte=5000000&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1"
      ]
for a in res:
    print(a)
    res = requests.get(a)
    html = res.text
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, features='html.parser')
    prices = soup.find_all(class_='offer-snippet__title')

    res_pr = []
    for pr in prices:
        sp = pr.find('span')
    
    res_pr.append(int(sp.text.replace(' ', '')))

    sum(res_pr)
    avg_price = sum(res_pr)/len(res_pr)
    print(avg_price)