from selenium import webdriver
from selenium.webdriver.support.ui import Select
from requests_html import HTMLSession, AsyncHTMLSession
import time

import config

base_url = 'https://www.supremenewyork.com'

def get_product_links():
    '''
    Returns list of elements "items",
    each containing a link to product detail page
    '''

    base_shop = base_url + '/shop'
    session = HTMLSession()
    r = session.get(base_shop)
    items = r.html.find('#shop-scroller', first=True).find('li')
    return items, session

print("Test")
