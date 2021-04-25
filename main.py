from services import parser, saver, analyst
from config import FIELDS, URLS


all_products = parser.get_all_products(URLS)

# saver.save_to_csv(all_products, FIELDS, path='files/')
saver.save_to_exel(all_products, FIELDS, path='files/')
