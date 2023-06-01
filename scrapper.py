import time, random, playwright.sync_api as sp
from bs4 import BeautifulSoup
from objects import *


def getAd(ad):
    # Ad
    result = Ad()
    result.id = (
        ad.find("div", {"class": "web_ui__ItemBox__box"})
        .get("data-testid")
        .split("--overlay-link")[0]
        .split("-")[-1]
    )
    result.url = ad.find("a", {"class": "web_ui__ItemBox__overlay"}).get("href")
    result.price = ad.find("h3").text[:-2]
    image = ad.find("div", {"class": "web_ui__ItemBox__image"}).find("img")
    result.title = image.get("alt")
    result.images = [image.get("src")]

    # Account
    account = Account()
    divAccount = ad.find(
        "a", {"class": "web_ui__Cell__cell web_ui__Cell__narrow web_ui__Cell__link"}
    )
    if divAccount == None:
        divAccount = ad.find("div", {"class": "web_ui__Cell__image"})
        urlSplit = divAccount.find("a").get("href").split("/member/")[1].split("-")
    else:
        urlSplit = divAccount.get("href").split("/member/")[1].split("-")
    account.id = urlSplit[0]
    account.username = urlSplit[1]
    account.profile_picture = divAccount.find("img").get("src")
    result.account = account
    return result


def scrap(item: Item, delay_range: tuple) -> list[Ad]:
    ads = []
    for keyword in item.keywords:
        browser = sp.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(
            f"https://www.vinted.fr/catalog?search_text={keyword}&price_from={item.price_range[0]}&currency=EUR&price_to={item.price_range[1]}&order=newest_first"
        )
        page.locator("button#onetrust-accept-btn-handler").click()
        soup = BeautifulSoup(page.content(), "html.parser").find_all(
            "div", {"data-testid": "grid-item"}
        )
        for ad in soup:
            ads.append(getAd(ad))
        browser.close()
        time.sleep(random.randint(delay_range[0], delay_range[1]))
    return ads
