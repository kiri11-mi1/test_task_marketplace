import requests
from bs4 import BeautifulSoup


URLS = [
    'https://www.wildberries.ru/catalog/15545307/detail.aspx?targetUrl=SP',
    'https://www.wildberries.ru/catalog/19957874/detail.aspx?targetUrl=XS',
    'https://www.wildberries.ru/catalog/19247096/detail.aspx?targetUrl=XS'
]


def get_date(soup: BeautifulSoup):
    pass


def get_link_to_image(soup: BeautifulSoup):
    return 'https:' + soup.find('img', class_ = 'preview-photo').get('src')


def get_product(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        return {'error': response.status_code}
    soup = BeautifulSoup(response.text, 'html.parser')

    return {
        'date': None,
        'link_to_image': get_link_to_image(soup),
        'link_to_product': None,
        'article_number': None,
        'price': None,
        'rating': None,
        'remainder': None,
        'comments_the_last_day': None
    }


def get_all_products():
    all_products = []
    for url in URLS:
        all_products.append(get_product(url))
    return all_products


if __name__ == '__main__':
    for prod in get_all_products():
        for key, value in prod.items():
            print(key, ' : ', value)
