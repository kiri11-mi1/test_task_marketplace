import requests
from bs4 import BeautifulSoup
from datetime import datetime


URLS = [
    'https://www.wildberries.ru/catalog/15545307/detail.aspx?targetUrl=SP',
    'https://www.wildberries.ru/catalog/19957874/detail.aspx?targetUrl=XS',
    'https://www.wildberries.ru/catalog/19247096/detail.aspx?targetUrl=XS',
    'https://www.wildberries.ru/catalog/10017305/detail.aspx?targetUrl=XS'
]


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    if response.status_code != 200:
        return response.status_code
    return BeautifulSoup(response.text, 'html.parser')


def get_comments_the_last_day(soup: BeautifulSoup, date: str) -> int:
    url = "https://www.wildberries.ru" + soup.find('a', {'id': 'a-Comments'}).get('href')
    if not (soup := get_soup(url)):
        return {'error': response.status_code}
    return len(list(filter(lambda div: date in div['content'],
                           soup.find_all('div', class_='time'))))


def get_rating(soup: BeautifulSoup) -> str:
    return soup.find('div', class_='product-rating').find('span').get_text(strip=True)


def get_price(soup: BeautifulSoup) -> str:
    return soup.find('span', class_='final-cost').get_text(strip=True)


def get_article_number(soup: BeautifulSoup) -> str:
    return soup.find('div', class_='article').find('span').get_text(strip=True)


def get_link_to_image(soup: BeautifulSoup) -> str:
    return 'https:' + soup.find('img', class_ = 'preview-photo').get('src')


def get_product(url: str) -> dict:
    '''Получение информации о продукте'''
    if not (soup := get_soup(url)):
        return {'error': response.status_code}

    current_date = str(datetime.now().date())
    return {
        'date': current_date,
        'link_to_image': get_link_to_image(soup),
        'link_to_product': url,
        'article_number': get_article_number(soup),
        'price': get_price(soup),
        'rating': get_rating(soup),
        'remainder': None,
        'comments_the_last_day': get_comments_the_last_day(soup, current_date),
    }


def get_all_products() -> list:
    all_products = []
    for url in URLS:
        all_products.append(get_product(url))
    return all_products


if __name__ == '__main__':
    # TO DO:
    # 1. Подрубить gevent
    # 2. Проверить почту и узнать что такое остаток
    # 3. Сделать замеры до и после gevent
    for prod in get_all_products():
        for key, value in prod.items():
            print(key, ' : ', value)
        print()
