import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.cn/dp/B07PRQS9QH/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=alienware&qid=1573223467&sr=8-1'

# Use Chrome chrome://version/ to check your user-agent,
# you can also use  IETF's tool page :https://tools.ietf.org/html/rfc2616#section-14.4 to choose header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',  # Do not track Request Header
    'Connection': 'close'
}


def track_our_price_and_send_mail():
    page = requests.get(URL, headers=headers)

    soup_obj = BeautifulSoup(page.content, 'html.parser')

    product_name = soup_obj.find(id='productTitle').get_text()
    product_price = soup_obj.find(id='priceblock_ourprice').get_text()

    # if the following code didn't work , try to replace , with blank
    # method 1: convert_product_price_string_to_float=float(product_price[0:5])
    # method 2
    convert_product_price_string_to_float = float(product_price[1:7].replace(",", ""))

    # if (convert_product_price_string_to_float <25000):
    #     send_a_mail_to_notify_me()

    # print(soup_obj.prettify())
    # print(product_name.strip())
    # print(convert_product_price_string_to_float)
    # print(type(convert_product_price_string_to_float))


