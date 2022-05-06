import json
import time

import requests
from bs4 import BeautifulSoup
import re

headers = {
    "user - agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 100.0.4896.127Safari / 537.36"
}
#rozetka_start
# rozetka_links = ['https://rozetka.com.ua/mobile-phones/c80003/producer=apple;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=huawei;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=motorola;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=oppo;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=oneplus;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=samsung;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=xiaomi;sell_status=available/',
#                  'https://rozetka.com.ua/mobile-phones/c80003/producer=zte;sell_status=available/']
# # def get_data(url, c):
#
# #
# #     req = requests.get(url, headers)
# #
# #     with open(f'data/rozetka_{c}.html', 'w', encoding='utf-8') as file:
# #         file.write(req.text)
# #
# # count = 1
# # for x in rozetka_links:
# #     get_data(x, count)
# #     count += 1
#
# producer = ['Apple', 'Huawei', 'Motorola', 'Oppo', 'Oneplus', 'Samsung', 'Xiaomi', 'Zte']
# rozetka_link = []
# count = 1
# product_price = []
# product_resolution = []
# product_hard_mem = []
# product_ram = []
# product_info = []
#
# with open('data/rozetka/rozetka_8.html', encoding='utf-8') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# links = soup.find_all('a', class_="goods-tile__picture ng-star-inserted")
# try:
#     product_price_find = soup.find_all('span', class_='goods-tile__price-value')
# except Exception:
#     product_price_find = None
#
# for price in product_price_find:
#     p = price.text
#     pr = p.replace('\xa0', '')
#     product_price.append(pr)
#     if len(product_price) == len(product_price_find):
#         break
#     else:
#         pass
#
# #     product_info.append(
# #         {
# #             "company": producer[0],
# #             "price": f'{p}',
# #             "url": '',
# #             "resolution": '',
# #             "hard_mem": '',
# #             "ram": '',
# #         }
# #     )
# # with open(f'data/product_info_0.json', 'a', encoding='utf-8') as file:
# #     json.dump(product_info, file, indent=4, ensure_ascii=False)
# for xl in links:
#     xl_link = xl.get('href')
#     rozetka_link.append(xl_link)
#     xl_link_char = xl_link + 'characteristics/'
#     req = requests.get(xl_link_char, headers)
#     page =xl_link.split('/')
#     page_name = page[3]
#     with open(f"data/{page_name}.html", encoding='utf-8') as file:
#         source = file.read()
#
#     soup = BeautifulSoup(source, 'lxml')
#
#     try:
#         product_resolution_find = soup.find('span', text=re.compile("Разрешение дисплея")).find_next().find_next().\
#             find_next().find('a', class_='ng-star-inserted').text
#     except Exception:
#         product_resolution_find = None
#     product_resolution.append(product_resolution_find)
#     # with open('data/product_info_0.json', encoding='utf-8') as f:
#     #     data = json.load(f)
#     # data[0]["resolution"] = product_resolution
#     # with open('data/product_info_0.json', 'w', encoding='utf-8') as f:
#     #     json.dump(data, f, ensure_ascii=False)
#
#     try:
#         product_hard_mem_find = soup.find('span', text=re.compile("Встроенная память")).find_next().find_next().\
#             find_next().find('a', class_='ng-star-inserted').text
#     except Exception:
#         product_hard_mem_find = None
#     product_hard_mem.append(product_hard_mem_find)
#     try:
#         product_ram_find = soup.find('span', text=re.compile("Оперативная память")).find_next().find_next(). \
#                                 find_next().find('a', class_='ng-star-inserted').text
#     except Exception:
#         product_ram_find = None
#     product_ram.append(product_ram_find)
#
#     # print(len(rozetka_link))
#     print(len(product_price))
#     # print(len(product_resolution))
#     # print(len(product_resolution))
#     # print(len(product_ram))
#
# for x in range(0, 60):
#     product_info.append(
#         {
#             "company": 'Zte',
#             "price": product_price[x],
#             "url": rozetka_link[x],
#             "resolution": product_resolution[x],
#             "hard_mem": product_hard_mem[x],
#             "ram": product_ram[x],
#         }
#     )
#     print(count)
#     count += 1
# with open('data/rozetka/product_info_8.json', 'a', encoding='utf-8') as file:
#     json.dump(product_info, file, indent=4, ensure_ascii=False)
#rozetka_finish

#allo_start
# allo_links = ['https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-apple/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-xiaomi/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-samsung/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-motorola/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-zte/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-huawei/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-oppo/',
#               'https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/proizvoditel-oneplus/']
#
# # def get_data(url, c):
# #
# #
# #     req = requests.get(url, headers)
# #
# #     with open(f'data/allo/allo_{c}.html', 'w', encoding='utf-8') as file:
# #         file.write(req.text)
# #
# # count = 0
# # for x in allo_links:
# #     get_data(x, count)
# #     count += 1
# product_allo_info = []
# product_brands = []
# product_links = []
# product_price = []
# product_resolution = []
# product_hard_mem = []
# product_ram = []
# for x in range(0, 8):
#     with open(f'data/allo/allo_{x}.html', encoding='utf-8') as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     links = soup.find_all('a', class_="product-card__title")
#     for xl in links:
#         p = xl.get('href')
#         product_links.append(p)
#         b = p.split('/')
#         c = b[-1].split('-')
#         product_brands.append(c[0].capitalize())
# for y in product_links:
#     # req = requests.get(y, headers)
#     b = y.split('/')
#     c = b[-1].split('.')
#     # with open(f'data/allo/{c[0]}.html', 'w', encoding='utf-8') as file:
#     #     file.write(req.text)
#     with open(f'data/allo/{c[0]}.html', encoding='utf-8') as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     try:
#         price = soup.find('span', class_='sum').text.strip()
#         pr = price.split(' ')
#         pr = pr[0].split('\xa0')
#         pr = pr[0] + pr[1]
#         product_price.append(pr)
#     except Exception:
#         product_price.append(None)
#
#     try:
#         resolution = soup.find(text=re.compile("Роздільна здатність дисплея")).find_next().text
#         product_resolution.append(resolution)
#     except Exception:
#         product_resolution.append(None)
#
#     try:
#         hard_mem = soup.find(text=re.compile("Внутрішня пам'ять")).find_next().text
#         try:
#             hard_mem = hard_mem.replace('Slim Box', '')
#             product_hard_mem.append(hard_mem)
#         except Exception:
#             product_hard_mem.append(hard_mem)
#     except Exception:
#         product_hard_mem.append(None)
#
#     try:
#         ram = soup.find(text=re.compile("Оперативна пам'ять")).find_next().text
#         product_ram.append(ram)
#     except Exception:
#         product_ram.append(None)
#
# z = len(product_links)
# # print(len(product_price))
# # print(len(product_resolution))
# # print(len(product_hard_mem))
# # print(len(product_ram))
#
# count = 1
# for x in range(0, z):
#     product_allo_info.append(
#         {
#             "company": product_brands[x],
#             "price": product_price[x],
#             "url": product_links[x],
#             "resolution": product_resolution[x],
#             "hard_mem": product_hard_mem[x],
#             "ram": product_ram[x],
#         }
#     )
#     print(count)
#     count += 1
# with open('data/allo/product_allo_info.json', 'a', encoding='utf-8') as file:
#     json.dump(product_allo_info, file, indent=4, ensure_ascii=False)
#allo_finish

#f start
# f_links = ['https://f.ua/ua/shop/mobilnye-telefony/apple/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/huawei/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/motorola/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/oppo/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/oneplus/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/samsung/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/xiaomi/?sticker=available',
#               'https://f.ua/ua/shop/mobilnye-telefony/zte/?sticker=available']
#
# # def get_data(url, c):
# #
# #
# #     req = requests.get(url, headers)
# #
# #     with open(f'data/f_ua/f_{c}.html', 'w', encoding='utf-8') as file:
# #         file.write(req.text)
# #
# # count = 0
# # for x in f_links:
# #     get_data(x, count)
# #     count += 1
# product_allo_info = []
# product_brands = []
# product_links = []
# product_price = []
# product_resolution = []
# product_hard_mem = []
# product_ram = []
# brand = ['APPLE', 'HUAWEI', 'MOTOROLA', 'OPPO', 'ONEPLUS', 'SAMSUNG', 'XIAOMI', 'ZTE']
# for x in range(0, 8):
#     with open(f'data/f_ua/f_{x}.html', encoding='utf-8') as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     links = soup.find_all('div', class_="title")
#     for xl in links:
#         prepare = xl.find('a', text=re.compile(f"{brand[x]}"))
#         if prepare != None:
#             a = prepare.get('href')
#             product_links.append(a)
#             product_brands.append(brand[x].capitalize())
#         else:
#             pass
# for y in product_links:
#     # req = requests.get(y, headers)
#     b = y.split('/')
#     c = b[-1].split('.')
#     # with open(f'data/f_ua/{c[0]}.html', 'w', encoding='utf-8') as file:
#     #     file.write(req.text)
#     with open(f'data/f_ua/{c[0]}.html', encoding='utf-8') as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     try:
#         price = soup.find('div', class_='price').find_next().find_next().find_next().text.strip()
#         price = price.split('₴')
#         price = price[0].replace(' ', '')
#         if price == 'Купити':
#             price = soup.find('div', class_='price').find_next().text.strip()
#             price = price.split('₴')
#             price = price[0].replace(' ', '')
#             product_price.append(price)
#         else:
#             product_price.append(price)
#     except Exception:
#         product_price.append(None)
#
#     try:
#         resolution = soup.find('td', class_='name', text=re.compile("Роздільна здатність")).find_next(text=re.compile("x"))
#         product_resolution.append(resolution)
#     except Exception:
#         product_resolution.append(None)
#
#     try:
#         hard_mem = soup.find('td', class_='name', text=re.compile("Об'єм внутрішньої пам'яті")).find_next().find_next()
#         hard_mem_res = hard_mem.text
#         product_hard_mem.append(hard_mem_res)
#     except Exception:
#         product_hard_mem.append(None)
#
#     try:
#         ram = soup.find('td', class_='name', text=re.compile("Об'єм оперативної пам'яті")).find_next()
#         ram_res = ram.text
#         product_ram.append(ram_res)
#     except Exception:
#         product_ram.append(None)
#
# z = len(product_brands)
# # print(len(product_links))
# # print(len(product_price))
# # print(len(product_resolution))
# # print(len(product_hard_mem))
# # print(len(product_ram))
# count = 1
# for x in range(0, z):
#     product_allo_info.append(
#         {
#             "company": product_brands[x],
#             "price": product_price[x],
#             "url": product_links[x],
#             "resolution": product_resolution[x],
#             "hard_mem": product_hard_mem[x],
#             "ram": product_ram[x],
#         }
#     )
#     print(count)
#     count += 1
# with open('data/f_ua/product_f_ua_info.json', 'a', encoding='utf-8') as file:
#     json.dump(product_allo_info, file, indent=4, ensure_ascii=False)
#f finish


with open(f'data/allo/product_allo_info.json', encoding='utf-8') as file:
    src = file.read()
work_dict = json.loads(src)
# print(len(work_dict))
for x in range(0, 224):
    a = work_dict[x]['resolution']
    b = a.split('x')
    print(b)
    c = int(b[0]) * int(b[1])
    print(c)
    work_dict[x]['resolution'] = c
    with open('data/allo/product_allo_info.json', 'w', encoding='utf-8') as file:
        json.dump(work_dict, file, indent=4, ensure_ascii=False)