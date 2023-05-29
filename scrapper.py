import playwright.sync_api
from playwright_stealth import stealth_sync
import json
from bs4 import BeautifulSoup
import time
import random


class Item():
    def __init__(self, name: str, keywords: list[str], price_range: tuple) -> None:
        self.name = name
        self.keywords = keywords
        self.price_range = price_range


class Account():
    def __init__(self) -> None:
        self.id = None
        self.username = None
        self.profile_picture = []
        self.rating_score = None
        self.rating_count = None


class Ad():
    def __init__(self) -> None:
        self.id = None
        self.title = None
        self.url = None
        self.price = None
        self.images = []
        self.account = Account()


def getAccount(link, browser):

    page = browser.new_page()
    stealth_sync(page)
    page.goto(link)
    soup = BeautifulSoup(page.content(), 'html.parser')
    account = Account()
    account.profile_picture = soup.find(
        'div', {'class': 'u-flexbox'}).find('img').get('src')
    json = soup.find('script', {'id': 'js-react-on-rails-context'})
    #account.id = json['pathname'].split('/member/')[0]
    # print(account.id)
    page.close()
    return account


def getAd(ad, browser):
    result = Ad()
    result.id = ad.find(
        'div', {'class': 'web_ui__ItemBox__box'}).get('data-testid')
    split = result.id.split('product-item-id-')
    if (len(split) > 1):
        result.id = split[1]  # ID
    else:
        result.id = result.id.split('item-')[1]
    print(result.id)
    thumbnail = ad.find(
        'a', {'class': 'web_ui__ItemBox__overlay'})
    result.url = thumbnail.get('href')  # URL
    split = thumbnail.get('title')
    result.title = split.split(', prix\xa0: ')[0]  # Title
    result.price = split.split(', prix\xa0: ')[1].split('\xa0€')[0]  # Price
    result.images = ad.find(
        'img', {'class': 'web_ui__Image__content'}).get('src')  # Images

    account = getAccount(ad.find(
        'a', {'class': 'web_ui__Cell__cell web_ui__Cell__narrow web_ui__Cell__link'}).get('href'), browser)

    return result


def scrap(item: Item, delay_range: tuple) -> list[Ad]:
    ads = []
    for keyword in item.keywords:
        with playwright.sync_api.sync_playwright() as sp:
            browser = sp.firefox.launch(headless=False, slow_mo=70)
            page = browser.new_page()
            stealth_sync(page)
            page.goto(
                f'https://www.vinted.fr/catalog?search_text={keyword}&price_from={item.price_range[0]}&currency=EUR&price_to={item.price_range[1]}&order=newest_first')
            page.locator('button#onetrust-accept-btn-handler').click()
            soup = BeautifulSoup(page.content(), 'html.parser').find_all(
                'div', {'data-testid': 'grid-item'})
            for ad in soup:
                ads.append(getAd(ad, browser))
            browser.close()
        time.sleep(random.randint(delay_range[0], delay_range[1]))
    return ads
